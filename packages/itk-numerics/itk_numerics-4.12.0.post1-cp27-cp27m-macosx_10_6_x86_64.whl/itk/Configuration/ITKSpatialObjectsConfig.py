depends = ('ITKPyBase', 'ITKTransform', 'ITKMesh', 'ITKImageFunction', 'ITKCommon', )
templates = (
  ('SpatialObjectProperty', 'itk::SpatialObjectProperty', 'itkSpatialObjectPropertyF', True, 'float'),
  ('AffineGeometryFrame', 'itk::AffineGeometryFrame', 'itkAffineGeometryFrameD2', True, 'double,2'),
  ('AffineGeometryFrame', 'itk::AffineGeometryFrame', 'itkAffineGeometryFrameD3', True, 'double,3'),
  ('MetaEvent', 'itk::MetaEvent', 'itkMetaEvent', True),
  ('SpatialObject', 'itk::SpatialObject', 'itkSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkSpatialObject2_Pointer', False, 'itk::SpatialObject< 2  >'),
  ('SpatialObject', 'itk::SpatialObject', 'itkSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkSpatialObject3_Pointer', False, 'itk::SpatialObject< 3  >'),
  ('CylinderSpatialObject', 'itk::CylinderSpatialObject', 'itkCylinderSpatialObject', True),
  ('TreeNode', 'itk::TreeNode', 'itkTreeNodeSO2', False, 'itk::SpatialObject< 2 >*'),
  ('TreeNode', 'itk::TreeNode', 'itkTreeNodeSO3', False, 'itk::SpatialObject< 3 >*'),
  ('SpatialObjectTreeNode', 'itk::SpatialObjectTreeNode', 'itkSpatialObjectTreeNode2', True, '2'),
  ('SpatialObjectTreeNode', 'itk::SpatialObjectTreeNode', 'itkSpatialObjectTreeNode3', True, '3'),
  ('SpatialObjectPoint', 'itk::SpatialObjectPoint', 'itkSpatialObjectPoint2', True, '2'),
  ('vector', 'std::vector', 'vectoritkSpatialObjectPoint2', False, 'itk::SpatialObjectPoint< 2  >'),
  ('SpatialObjectPoint', 'itk::SpatialObjectPoint', 'itkSpatialObjectPoint3', True, '3'),
  ('vector', 'std::vector', 'vectoritkSpatialObjectPoint3', False, 'itk::SpatialObjectPoint< 3  >'),
  ('ContourSpatialObjectPoint', 'itk::ContourSpatialObjectPoint', 'itkContourSpatialObjectPoint2', True, '2'),
  ('vector', 'std::vector', 'vectoritkContourSpatialObjectPoint2', False, 'itk::ContourSpatialObjectPoint< 2  >'),
  ('ContourSpatialObjectPoint', 'itk::ContourSpatialObjectPoint', 'itkContourSpatialObjectPoint3', True, '3'),
  ('vector', 'std::vector', 'vectoritkContourSpatialObjectPoint3', False, 'itk::ContourSpatialObjectPoint< 3  >'),
  ('DTITubeSpatialObjectPoint', 'itk::DTITubeSpatialObjectPoint', 'itkDTITubeSpatialObjectPoint3', True, '3'),
  ('VesselTubeSpatialObjectPoint', 'itk::VesselTubeSpatialObjectPoint', 'itkVesselTubeSpatialObjectPoint2', True, '2'),
  ('VesselTubeSpatialObjectPoint', 'itk::VesselTubeSpatialObjectPoint', 'itkVesselTubeSpatialObjectPoint3', True, '3'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObject2', True, '2'),
  ('PointBasedSpatialObject', 'itk::PointBasedSpatialObject', 'itkPointBasedSpatialObject3', True, '3'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject2UC', True, '2,unsigned char'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject2SS', True, '2,signed short'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject2F', True, '2,float'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject3UC', True, '3,unsigned char'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject3SS', True, '3,signed short'),
  ('ImageSpatialObject', 'itk::ImageSpatialObject', 'itkImageSpatialObject3F', True, '3,float'),
  ('BlobSpatialObject', 'itk::BlobSpatialObject', 'itkBlobSpatialObject2', True, '2'),
  ('BlobSpatialObject', 'itk::BlobSpatialObject', 'itkBlobSpatialObject3', True, '3'),
  ('PolygonSpatialObject', 'itk::PolygonSpatialObject', 'itkPolygonSpatialObject2', True, '2'),
  ('PolygonSpatialObject', 'itk::PolygonSpatialObject', 'itkPolygonSpatialObject3', True, '3'),
  ('ArrowSpatialObject', 'itk::ArrowSpatialObject', 'itkArrowSpatialObject2', True, '2'),
  ('ArrowSpatialObject', 'itk::ArrowSpatialObject', 'itkArrowSpatialObject3', True, '3'),
  ('BoxSpatialObject', 'itk::BoxSpatialObject', 'itkBoxSpatialObject2', True, '2'),
  ('BoxSpatialObject', 'itk::BoxSpatialObject', 'itkBoxSpatialObject3', True, '3'),
  ('ContourSpatialObject', 'itk::ContourSpatialObject', 'itkContourSpatialObject2', True, '2'),
  ('ContourSpatialObject', 'itk::ContourSpatialObject', 'itkContourSpatialObject3', True, '3'),
  ('DTITubeSpatialObject', 'itk::DTITubeSpatialObject', 'itkDTITubeSpatialObject3', True, '3'),
  ('EllipseSpatialObject', 'itk::EllipseSpatialObject', 'itkEllipseSpatialObject2', True, '2'),
  ('list', 'std::list', 'listitkEllipseSpatialObject2_Pointer', False, 'itk::EllipseSpatialObject< 2  >'),
  ('EllipseSpatialObject', 'itk::EllipseSpatialObject', 'itkEllipseSpatialObject3', True, '3'),
  ('list', 'std::list', 'listitkEllipseSpatialObject3_Pointer', False, 'itk::EllipseSpatialObject< 3  >'),
  ('GaussianSpatialObject', 'itk::GaussianSpatialObject', 'itkGaussianSpatialObject2', True, '2'),
  ('GaussianSpatialObject', 'itk::GaussianSpatialObject', 'itkGaussianSpatialObject3', True, '3'),
  ('GroupSpatialObject', 'itk::GroupSpatialObject', 'itkGroupSpatialObject2', True, '2'),
  ('GroupSpatialObject', 'itk::GroupSpatialObject', 'itkGroupSpatialObject3', True, '3'),
  ('ImageMaskSpatialObject', 'itk::ImageMaskSpatialObject', 'itkImageMaskSpatialObject2', True, '2'),
  ('ImageMaskSpatialObject', 'itk::ImageMaskSpatialObject', 'itkImageMaskSpatialObject3', True, '3'),
  ('LandmarkSpatialObject', 'itk::LandmarkSpatialObject', 'itkLandmarkSpatialObject2', True, '2'),
  ('LandmarkSpatialObject', 'itk::LandmarkSpatialObject', 'itkLandmarkSpatialObject3', True, '3'),
  ('LineSpatialObject', 'itk::LineSpatialObject', 'itkLineSpatialObject2', True, '2'),
  ('LineSpatialObject', 'itk::LineSpatialObject', 'itkLineSpatialObject3', True, '3'),
  ('LineSpatialObjectPoint', 'itk::LineSpatialObjectPoint', 'itkLineSpatialObjectPoint2', True, '2'),
  ('vector', 'std::vector', 'vectoritkLineSpatialObjectPoint2', False, 'itk::LineSpatialObjectPoint< 2  >'),
  ('LineSpatialObjectPoint', 'itk::LineSpatialObjectPoint', 'itkLineSpatialObjectPoint3', True, '3'),
  ('vector', 'std::vector', 'vectoritkLineSpatialObjectPoint3', False, 'itk::LineSpatialObjectPoint< 3  >'),
  ('MetaConverterBase', 'itk::MetaConverterBase', 'itkMetaConverterBase2', True, '2'),
  ('MetaConverterBase', 'itk::MetaConverterBase', 'itkMetaConverterBase3', True, '3'),
  ('PlaneSpatialObject', 'itk::PlaneSpatialObject', 'itkPlaneSpatialObject2', True, '2'),
  ('PlaneSpatialObject', 'itk::PlaneSpatialObject', 'itkPlaneSpatialObject3', True, '3'),
  ('PolygonGroupSpatialObject', 'itk::PolygonGroupSpatialObject', 'itkPolygonGroupSpatialObject2', True, '2'),
  ('PolygonGroupSpatialObject', 'itk::PolygonGroupSpatialObject', 'itkPolygonGroupSpatialObject3', True, '3'),
  ('SceneSpatialObject', 'itk::SceneSpatialObject', 'itkSceneSpatialObject2', True, '2'),
  ('SceneSpatialObject', 'itk::SceneSpatialObject', 'itkSceneSpatialObject3', True, '3'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO2ISS2', True, 'itk::SpatialObject< 2 >,itk::Image< signed short,2 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO2IUC2', True, 'itk::SpatialObject< 2 >,itk::Image< unsigned char,2 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO2IF2', True, 'itk::SpatialObject< 2 >,itk::Image< float,2 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO3ISS3', True, 'itk::SpatialObject< 3 >,itk::Image< signed short,3 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO3IUC3', True, 'itk::SpatialObject< 3 >,itk::Image< unsigned char,3 >'),
  ('SpatialObjectToImageFilter', 'itk::SpatialObjectToImageFilter', 'itkSpatialObjectToImageFilterSO3IF3', True, 'itk::SpatialObject< 3 >,itk::Image< float,3 >'),
  ('SurfaceSpatialObject', 'itk::SurfaceSpatialObject', 'itkSurfaceSpatialObject2', True, '2'),
  ('SurfaceSpatialObject', 'itk::SurfaceSpatialObject', 'itkSurfaceSpatialObject3', True, '3'),
  ('SurfaceSpatialObjectPoint', 'itk::SurfaceSpatialObjectPoint', 'itkSurfaceSpatialObjectPoint2', True, '2'),
  ('vector', 'std::vector', 'vectoritkSurfaceSpatialObjectPoint2', False, 'itk::SurfaceSpatialObjectPoint< 2  >'),
  ('SurfaceSpatialObjectPoint', 'itk::SurfaceSpatialObjectPoint', 'itkSurfaceSpatialObjectPoint3', True, '3'),
  ('vector', 'std::vector', 'vectoritkSurfaceSpatialObjectPoint3', False, 'itk::SurfaceSpatialObjectPoint< 3  >'),
  ('TubeSpatialObjectPoint', 'itk::TubeSpatialObjectPoint', 'itkTubeSpatialObjectPoint2', True, '2'),
  ('TubeSpatialObjectPoint', 'itk::TubeSpatialObjectPoint', 'itkTubeSpatialObjectPoint3', True, '3'),
  ('VesselTubeSpatialObject', 'itk::VesselTubeSpatialObject', 'itkVesselTubeSpatialObject2', True, '2'),
  ('VesselTubeSpatialObject', 'itk::VesselTubeSpatialObject', 'itkVesselTubeSpatialObject3', True, '3'),
)
