depends = ('ITKPyBase', 'ITKSmoothing', 'ITKImageIntensity', )
templates = (
  ('DifferenceOfGaussiansGradientImageFilter', 'itk::DifferenceOfGaussiansGradientImageFilter', 'itkDifferenceOfGaussiansGradientImageFilterISS2F', True, 'itk::Image< signed short,2 >, float'),
  ('DifferenceOfGaussiansGradientImageFilter', 'itk::DifferenceOfGaussiansGradientImageFilter', 'itkDifferenceOfGaussiansGradientImageFilterIUC2F', True, 'itk::Image< unsigned char,2 >, float'),
  ('DifferenceOfGaussiansGradientImageFilter', 'itk::DifferenceOfGaussiansGradientImageFilter', 'itkDifferenceOfGaussiansGradientImageFilterIF2F', True, 'itk::Image< float,2 >, float'),
  ('DifferenceOfGaussiansGradientImageFilter', 'itk::DifferenceOfGaussiansGradientImageFilter', 'itkDifferenceOfGaussiansGradientImageFilterISS3F', True, 'itk::Image< signed short,3 >, float'),
  ('DifferenceOfGaussiansGradientImageFilter', 'itk::DifferenceOfGaussiansGradientImageFilter', 'itkDifferenceOfGaussiansGradientImageFilterIUC3F', True, 'itk::Image< unsigned char,3 >, float'),
  ('DifferenceOfGaussiansGradientImageFilter', 'itk::DifferenceOfGaussiansGradientImageFilter', 'itkDifferenceOfGaussiansGradientImageFilterIF3F', True, 'itk::Image< float,3 >, float'),
  ('GradientImageFilter', 'itk::GradientImageFilter', 'itkGradientImageFilterISS2FF', True, 'itk::Image< signed short,2 >,float,float'),
  ('GradientImageFilter', 'itk::GradientImageFilter', 'itkGradientImageFilterIUC2FF', True, 'itk::Image< unsigned char,2 >,float,float'),
  ('GradientImageFilter', 'itk::GradientImageFilter', 'itkGradientImageFilterIF2FF', True, 'itk::Image< float,2 >,float,float'),
  ('GradientImageFilter', 'itk::GradientImageFilter', 'itkGradientImageFilterISS3FF', True, 'itk::Image< signed short,3 >,float,float'),
  ('GradientImageFilter', 'itk::GradientImageFilter', 'itkGradientImageFilterIUC3FF', True, 'itk::Image< unsigned char,3 >,float,float'),
  ('GradientImageFilter', 'itk::GradientImageFilter', 'itkGradientImageFilterIF3FF', True, 'itk::Image< float,3 >,float,float'),
  ('GradientMagnitudeImageFilter', 'itk::GradientMagnitudeImageFilter', 'itkGradientMagnitudeImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('GradientMagnitudeImageFilter', 'itk::GradientMagnitudeImageFilter', 'itkGradientMagnitudeImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('GradientMagnitudeImageFilter', 'itk::GradientMagnitudeImageFilter', 'itkGradientMagnitudeImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('GradientMagnitudeImageFilter', 'itk::GradientMagnitudeImageFilter', 'itkGradientMagnitudeImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('GradientMagnitudeImageFilter', 'itk::GradientMagnitudeImageFilter', 'itkGradientMagnitudeImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('GradientMagnitudeImageFilter', 'itk::GradientMagnitudeImageFilter', 'itkGradientMagnitudeImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('GradientMagnitudeRecursiveGaussianImageFilter', 'itk::GradientMagnitudeRecursiveGaussianImageFilter', 'itkGradientMagnitudeRecursiveGaussianImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('GradientMagnitudeRecursiveGaussianImageFilter', 'itk::GradientMagnitudeRecursiveGaussianImageFilter', 'itkGradientMagnitudeRecursiveGaussianImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('GradientMagnitudeRecursiveGaussianImageFilter', 'itk::GradientMagnitudeRecursiveGaussianImageFilter', 'itkGradientMagnitudeRecursiveGaussianImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('GradientMagnitudeRecursiveGaussianImageFilter', 'itk::GradientMagnitudeRecursiveGaussianImageFilter', 'itkGradientMagnitudeRecursiveGaussianImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('GradientMagnitudeRecursiveGaussianImageFilter', 'itk::GradientMagnitudeRecursiveGaussianImageFilter', 'itkGradientMagnitudeRecursiveGaussianImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('GradientMagnitudeRecursiveGaussianImageFilter', 'itk::GradientMagnitudeRecursiveGaussianImageFilter', 'itkGradientMagnitudeRecursiveGaussianImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('GradientRecursiveGaussianImageFilter', 'itk::GradientRecursiveGaussianImageFilter', 'itkGradientRecursiveGaussianImageFilterISS2ICVF22', True, 'itk::Image< signed short,2 >,itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('GradientRecursiveGaussianImageFilter', 'itk::GradientRecursiveGaussianImageFilter', 'itkGradientRecursiveGaussianImageFilterIUC2ICVF22', True, 'itk::Image< unsigned char,2 >,itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('GradientRecursiveGaussianImageFilter', 'itk::GradientRecursiveGaussianImageFilter', 'itkGradientRecursiveGaussianImageFilterIF2ICVF22', True, 'itk::Image< float,2 >,itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('GradientRecursiveGaussianImageFilter', 'itk::GradientRecursiveGaussianImageFilter', 'itkGradientRecursiveGaussianImageFilterIVF22ICVF42', True, 'itk::Image< itk::Vector< float,2 >,2 >,itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('GradientRecursiveGaussianImageFilter', 'itk::GradientRecursiveGaussianImageFilter', 'itkGradientRecursiveGaussianImageFilterISS3ICVF23', True, 'itk::Image< signed short,3 >,itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('GradientRecursiveGaussianImageFilter', 'itk::GradientRecursiveGaussianImageFilter', 'itkGradientRecursiveGaussianImageFilterIUC3ICVF23', True, 'itk::Image< unsigned char,3 >,itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('GradientRecursiveGaussianImageFilter', 'itk::GradientRecursiveGaussianImageFilter', 'itkGradientRecursiveGaussianImageFilterIF3ICVF23', True, 'itk::Image< float,3 >,itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('GradientRecursiveGaussianImageFilter', 'itk::GradientRecursiveGaussianImageFilter', 'itkGradientRecursiveGaussianImageFilterIVF23ICVF43', True, 'itk::Image< itk::Vector< float,2 >,3 >,itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('VectorGradientMagnitudeImageFilter', 'itk::VectorGradientMagnitudeImageFilter', 'itkVectorGradientMagnitudeImageFilterIVF22F', True, 'itk::Image< itk::Vector< float,2 >,2 >, float'),
  ('VectorGradientMagnitudeImageFilter', 'itk::VectorGradientMagnitudeImageFilter', 'itkVectorGradientMagnitudeImageFilterIVF33F', True, 'itk::Image< itk::Vector< float,3 >,3 >, float'),
)
