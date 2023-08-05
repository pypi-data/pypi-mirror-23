depends = ('ITKPyBase', 'ITKImageFilterBase', )
templates = (
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterISS2VISS2', True, 'itk::Image< signed short,2 >, itk::VectorImage< signed short,2 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIUC2VIUC2', True, 'itk::Image< unsigned char,2 >, itk::VectorImage< unsigned char,2 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIF2VIF2', True, 'itk::Image< float,2 >, itk::VectorImage< float,2 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterISS3VISS3', True, 'itk::Image< signed short,3 >, itk::VectorImage< signed short,3 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIUC3VIUC3', True, 'itk::Image< unsigned char,3 >, itk::VectorImage< unsigned char,3 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIF3VIF3', True, 'itk::Image< float,3 >, itk::VectorImage< float,3 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIF2ICVF22', True, 'itk::Image< float,2 >, itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIF2ICVF32', True, 'itk::Image< float,2 >, itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIF2ICVF42', True, 'itk::Image< float,2 >, itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIF3ICVF23', True, 'itk::Image< float,3 >, itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIF3ICVF33', True, 'itk::Image< float,3 >, itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIF3ICVF43', True, 'itk::Image< float,3 >, itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIF2IVF22', True, 'itk::Image< float,2 >, itk::Image< itk::Vector< float,2 >,2 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIF2IVF32', True, 'itk::Image< float,2 >, itk::Image< itk::Vector< float,3 >,2 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIF2IVF42', True, 'itk::Image< float,2 >, itk::Image< itk::Vector< float,4 >,2 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIF3IVF23', True, 'itk::Image< float,3 >, itk::Image< itk::Vector< float,2 >,3 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIF3IVF33', True, 'itk::Image< float,3 >, itk::Image< itk::Vector< float,3 >,3 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIF3IVF43', True, 'itk::Image< float,3 >, itk::Image< itk::Vector< float,4 >,3 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIUC2IRGBAUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< itk::RGBAPixel< unsigned char >,2 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIUC3IRGBAUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< itk::RGBAPixel< unsigned char >,3 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIUC2IRGBUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('ComposeImageFilter', 'itk::ComposeImageFilter', 'itkComposeImageFilterIUC3IRGBUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('JoinSeriesImageFilter', 'itk::JoinSeriesImageFilter', 'itkJoinSeriesImageFilterISS2ISS3', True, 'itk::Image< signed short,2 >,itk::Image< signed short,3 >'),
  ('JoinSeriesImageFilter', 'itk::JoinSeriesImageFilter', 'itkJoinSeriesImageFilterIUC2IUC3', True, 'itk::Image< unsigned char,2 >,itk::Image< unsigned char,3 >'),
  ('JoinSeriesImageFilter', 'itk::JoinSeriesImageFilter', 'itkJoinSeriesImageFilterIF2IF3', True, 'itk::Image< float,2 >,itk::Image< float,3 >'),
)
