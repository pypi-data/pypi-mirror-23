depends = ('ITKPyBase', 'ITKSmoothing', 'ITKMesh', 'ITKImageStatistics', 'ITKImageSources', 'ITKImageGradient', )
templates = (
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterISS2', True, 'itk::Image< signed short,2 >'),
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterISS3', True, 'itk::Image< signed short,3 >'),
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterIF2', True, 'itk::Image< float,2 >'),
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterIF3', True, 'itk::Image< float,3 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('CannyEdgeDetectionImageFilter', 'itk::CannyEdgeDetectionImageFilter', 'itkCannyEdgeDetectionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('CannyEdgeDetectionImageFilter', 'itk::CannyEdgeDetectionImageFilter', 'itkCannyEdgeDetectionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('DerivativeImageFilter', 'itk::DerivativeImageFilter', 'itkDerivativeImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('DerivativeImageFilter', 'itk::DerivativeImageFilter', 'itkDerivativeImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('DerivativeImageFilter', 'itk::DerivativeImageFilter', 'itkDerivativeImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('DerivativeImageFilter', 'itk::DerivativeImageFilter', 'itkDerivativeImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('GradientVectorFlowImageFilter', 'itk::GradientVectorFlowImageFilter', 'itkGradientVectorFlowImageFilterIVF22IVF22F', True, 'itk::Image< itk::Vector< float,2 >,2 >, itk::Image< itk::Vector< float,2 >,2 >, float'),
  ('GradientVectorFlowImageFilter', 'itk::GradientVectorFlowImageFilter', 'itkGradientVectorFlowImageFilterICVF22ICVF22F', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >, itk::Image< itk::CovariantVector< float,2 >,2 >, float'),
  ('GradientVectorFlowImageFilter', 'itk::GradientVectorFlowImageFilter', 'itkGradientVectorFlowImageFilterIVF33IVF33F', True, 'itk::Image< itk::Vector< float,3 >,3 >, itk::Image< itk::Vector< float,3 >,3 >, float'),
  ('GradientVectorFlowImageFilter', 'itk::GradientVectorFlowImageFilter', 'itkGradientVectorFlowImageFilterICVF33ICVF33F', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >, itk::Image< itk::CovariantVector< float,3 >,3 >, float'),
  ('Hessian3DToVesselnessMeasureImageFilter', 'itk::Hessian3DToVesselnessMeasureImageFilter', 'itkHessian3DToVesselnessMeasureImageFilterSS', True, 'signed short'),
  ('Hessian3DToVesselnessMeasureImageFilter', 'itk::Hessian3DToVesselnessMeasureImageFilter', 'itkHessian3DToVesselnessMeasureImageFilterUC', True, 'unsigned char'),
  ('Hessian3DToVesselnessMeasureImageFilter', 'itk::Hessian3DToVesselnessMeasureImageFilter', 'itkHessian3DToVesselnessMeasureImageFilterF', True, 'float'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD22ISS2', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >, itk::Image< signed short,2 >'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD22IUC2', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >, itk::Image< unsigned char,2 >'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD22IF2', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >, itk::Image< float,2 >'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD33ISS3', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >, itk::Image< signed short,3 >'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD33IUC3', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >, itk::Image< unsigned char,3 >'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD33IF3', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >, itk::Image< float,3 >'),
  ('HoughTransform2DCirclesImageFilter', 'itk::HoughTransform2DCirclesImageFilter', 'itkHoughTransform2DCirclesImageFilterFF', True, 'float, float'),
  ('HoughTransform2DLinesImageFilter', 'itk::HoughTransform2DLinesImageFilter', 'itkHoughTransform2DLinesImageFilterFF', True, 'float, float'),
  ('LaplacianImageFilter', 'itk::LaplacianImageFilter', 'itkLaplacianImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('LaplacianImageFilter', 'itk::LaplacianImageFilter', 'itkLaplacianImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('MaskFeaturePointSelectionFilter', 'itk::MaskFeaturePointSelectionFilter', 'itkMaskFeaturePointSelectionFilterIF3', True, 'itk::Image< float,3 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('SobelEdgeDetectionImageFilter', 'itk::SobelEdgeDetectionImageFilter', 'itkSobelEdgeDetectionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SobelEdgeDetectionImageFilter', 'itk::SobelEdgeDetectionImageFilter', 'itkSobelEdgeDetectionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ZeroCrossingBasedEdgeDetectionImageFilter', 'itk::ZeroCrossingBasedEdgeDetectionImageFilter', 'itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ZeroCrossingBasedEdgeDetectionImageFilter', 'itk::ZeroCrossingBasedEdgeDetectionImageFilter', 'itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ZeroCrossingImageFilter', 'itk::ZeroCrossingImageFilter', 'itkZeroCrossingImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('ZeroCrossingImageFilter', 'itk::ZeroCrossingImageFilter', 'itkZeroCrossingImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('ZeroCrossingImageFilter', 'itk::ZeroCrossingImageFilter', 'itkZeroCrossingImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ZeroCrossingImageFilter', 'itk::ZeroCrossingImageFilter', 'itkZeroCrossingImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
)
