import unittest
from os import walk, path
import rasterio
import pytest
import numpy as np

from geopyspark.geotrellis.constants import LayerType, CellType
from geopyspark.tests.python_test_utils import geotiff_test_path
from geopyspark.geotrellis import Extent, ProjectedExtent, Tile
from geopyspark.geotrellis.geotiff import get
from geopyspark.geotrellis.layer import RasterLayer
from geopyspark.tests.base_test_class import BaseTestClass


class GeoTiffIOTest(object):
    def get_filepaths(self, dir_path):
        files = []

        for (fd, dn, filenames) in walk(dir_path):
            files.extend(filenames)

        return [path.join(dir_path, x) for x in files]

    def read_geotiff_rasterio(self, paths, windowed):
        rasterio_tiles = []

        windows = [((0, 256), (0, 256)),
                   ((256, 512), (0, 256)),
                   ((0, 256), (256, 512)),
                   ((256, 512), (256, 512))]

        for f in paths:
            with rasterio.open(f) as src:
                if not windowed:
                    rasterio_tiles.append({'cells': src.read(),
                                           'no_data_value': src.nodata})
                else:
                    for window in windows:
                        rasterio_tiles.append(
                            {'cells': src.read(window=window),
                             'no_data_value': src.nodata})

        return rasterio_tiles

class Multiband(GeoTiffIOTest, BaseTestClass):
    dir_path = geotiff_test_path("one-month-tiles-multiband/")
    result = get(LayerType.SPATIAL, dir_path)

    @pytest.fixture(autouse=True)
    def tearDown(self):
        yield
        BaseTestClass.pysc._gateway.close()

    def test_to_numpy_rdd(self, option=None):
        pyrdd = self.result.to_numpy_rdd()
        (key, tile) = pyrdd.first()
        self.assertEqual(tile.cells.shape, (2, 512, 512))

    def test_collect_metadata(self, options=None):
        md = self.result.collect_metadata()
        self.assertTrue('+proj=longlat' in md.crs)
        self.assertTrue('+datum=WGS84' in md.crs)

    def test_reproject(self, options=None):
        tiles = self.result.reproject("EPSG:3857")
        md = tiles.collect_metadata()
        self.assertTrue('+proj=merc' in md.crs)

    '''

    def test_to_int(self):
        arr = np.array([[0.4324323432124, 0.0, 0.0],
                        [1.0, 1.0, 1.0]], dtype=float)

        epsg_code = 3857
        extent = {'xmin': 0.0, 'ymin': 0.0, 'xmax': 10.0, 'ymax': 10.0}
        projected_extent = {'extent': extent, 'epsg': epsg_code}

        tile = {'data': arr, 'no_data_value': float('nan')}
        rdd = BaseTestClass.pysc.parallelize([(projected_extent, tile)])
        raster_rdd = RasterRDD.from_numpy_rdd(LayerType.SPATIAL, rdd)

        converted = raster_rdd.convert_data_type(INT32)
        arr = converted.to_numpy_rdd().first()[1]['data']

        self.assertEqual(arr.dtype, np.int64)

    def test_to_boolraw(self):
        converted = self.result.convert_data_type(BOOLRAW)
        arr = converted.to_numpy_rdd().first()[1]['data']

        self.assertEqual(arr.dtype, np.uint8)
    '''

    def test_to_ud_ubyte(self):
        arr = np.array([[0.4324323432124, 0.0, 0.0],
                        [1.0, 1.0, 1.0]], dtype=float)

        epsg_code = 3857
        extent = Extent(0.0, 0.0, 10.0, 10.0)
        projected_extent = ProjectedExtent(extent, epsg_code)

        tile = Tile(arr, 'FLOAT',float('nan'))
        rdd = BaseTestClass.pysc.parallelize([(projected_extent, tile)])
        raster_rdd = RasterLayer.from_numpy_rdd(LayerType.SPATIAL, rdd)

        converted = raster_rdd.convert_data_type(CellType.UINT8, no_data_value=-1)
        tile = converted.to_numpy_rdd().first()
        no_data = tile[1].no_data_value

        self.assertEqual(no_data, -1)

    def test_no_data_deserialization(self):
        arr = np.int16([[[-32768, -32768, -32768, -32768],
                         [-32768, -32768, -32768, -32768],
                         [-32768, -32768, -32768, -32768],
                         [-32768, -32768, -32768, -32768]]])

        epsg_code = 3857
        extent = Extent(0.0, 0.0, 10.0, 10.0)
        projected_extent = ProjectedExtent(extent, epsg_code)

        tile = Tile(arr, 'SHORT', -32768)
        rdd = BaseTestClass.pysc.parallelize([(projected_extent, tile)])
        raster_layer = RasterLayer.from_numpy_rdd(LayerType.SPATIAL, rdd)

        actual_tile = raster_layer.to_numpy_rdd().first()[1]

        self.assertEqual(actual_tile.cell_type, tile.cell_type)
        self.assertEqual(actual_tile.no_data_value, tile.no_data_value)
        self.assertTrue((actual_tile.cells == tile.cells).all())


if __name__ == "__main__":
    unittest.main()
