depends = ('ITKPyBase', 'ITKImageFunction', )
templates = (
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
)
