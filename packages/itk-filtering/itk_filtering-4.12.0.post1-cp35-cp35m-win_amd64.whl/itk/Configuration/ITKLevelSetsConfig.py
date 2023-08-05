depends = ('ITKPyBase', 'ITKThresholding', 'ITKOptimizers', 'ITKNarrowBand', 'ITKImageFeature', 'ITKImageCompare', 'ITKIOImageBase', 'ITKFiniteDifference', 'ITKFastMarching', 'ITKDistanceMap', 'ITKAnisotropicSmoothing', )
templates = (
  ('LevelSetFunction', 'itk::LevelSetFunction', 'itkLevelSetFunctionIF2', True, 'itk::Image< float,2 >'),
  ('LevelSetFunction', 'itk::LevelSetFunction', 'itkLevelSetFunctionIF3', True, 'itk::Image< float,3 >'),
  ('SparseFieldLevelSetImageFilter', 'itk::SparseFieldLevelSetImageFilter', 'itkSparseFieldLevelSetImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SparseFieldLevelSetImageFilter', 'itk::SparseFieldLevelSetImageFilter', 'itkSparseFieldLevelSetImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('SparseFieldLevelSetNode', 'itk::SparseFieldLevelSetNode', 'itkSparseFieldLevelSetNodeI2', False, 'itk::Index< 2 >'),
  ('SparseFieldLevelSetNode', 'itk::SparseFieldLevelSetNode', 'itkSparseFieldLevelSetNodeI3', False, 'itk::Index< 3 >'),
  ('SparseFieldLayer', 'itk::SparseFieldLayer', 'itkSparseFieldLayerSFLSNI2', False, 'itk::SparseFieldLevelSetNode< itk::Index< 2 > >'),
  ('SparseFieldLayer', 'itk::SparseFieldLayer', 'itkSparseFieldLayerSFLSNI3', False, 'itk::SparseFieldLevelSetNode< itk::Index< 3 > >'),
  ('NormalBandNode', 'itk::NormalBandNode', 'itkNormalBandNodeIF2', False, 'itk::Image< float,2 >'),
  ('NormalBandNode', 'itk::NormalBandNode', 'itkNormalBandNodeIF3', False, 'itk::Image< float,3 >'),
  ('Image', 'itk::Image', 'itkImageNBNIF22', False, 'itk::NormalBandNode< itk::Image< float,2 > >*, 2'),
  ('Image', 'itk::Image', 'itkImageNBNIF33', False, 'itk::NormalBandNode< itk::Image< float,3 > >*, 3'),
  ('SparseFieldFourthOrderLevelSetImageFilter', 'itk::SparseFieldFourthOrderLevelSetImageFilter', 'itkSparseFieldFourthOrderLevelSetImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SparseFieldFourthOrderLevelSetImageFilter', 'itk::SparseFieldFourthOrderLevelSetImageFilter', 'itkSparseFieldFourthOrderLevelSetImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('SparseImage', 'itk::SparseImage', 'itkSparseImageNBNIF22', False, 'itk::NormalBandNode< itk::Image< float,2 > >, 2'),
  ('SparseImage', 'itk::SparseImage', 'itkSparseImageNBNIF33', False, 'itk::NormalBandNode< itk::Image< float,3 > >, 3'),
  ('LevelSetFunctionWithRefitTerm', 'itk::LevelSetFunctionWithRefitTerm', 'itkLevelSetFunctionWithRefitTermIF2SINBNIF22', True, 'itk::Image< float,2 >, itk::SparseImage< itk::NormalBandNode< itk::Image< float,2 > >, 2 >'),
  ('LevelSetFunctionWithRefitTerm', 'itk::LevelSetFunctionWithRefitTerm', 'itkLevelSetFunctionWithRefitTermIF3SINBNIF33', True, 'itk::Image< float,3 >, itk::SparseImage< itk::NormalBandNode< itk::Image< float,3 > >, 3 >'),
  ('SparseFieldLayer', 'itk::SparseFieldLayer', 'itkSparseFieldLayerNBNIF2', False, 'itk::NormalBandNode< itk::Image< float,2 > >'),
  ('SparseFieldLayer', 'itk::SparseFieldLayer', 'itkSparseFieldLayerNBNIF3', False, 'itk::NormalBandNode< itk::Image< float,3 > >'),
  ('SegmentationLevelSetImageFilter', 'itk::SegmentationLevelSetImageFilter', 'itkSegmentationLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('SegmentationLevelSetImageFilter', 'itk::SegmentationLevelSetImageFilter', 'itkSegmentationLevelSetImageFilterIF2IVF22F', True, 'itk::Image< float,2 >,itk::Image< itk::Vector< float,2 >,2 >,float'),
  ('SegmentationLevelSetImageFilter', 'itk::SegmentationLevelSetImageFilter', 'itkSegmentationLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('SegmentationLevelSetImageFilter', 'itk::SegmentationLevelSetImageFilter', 'itkSegmentationLevelSetImageFilterIF3IVF33F', True, 'itk::Image< float,3 >,itk::Image< itk::Vector< float,3 >,3 >,float'),
  ('ShapePriorSegmentationLevelSetImageFilter', 'itk::ShapePriorSegmentationLevelSetImageFilter', 'itkShapePriorSegmentationLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('ShapePriorSegmentationLevelSetImageFilter', 'itk::ShapePriorSegmentationLevelSetImageFilter', 'itkShapePriorSegmentationLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('AnisotropicFourthOrderLevelSetImageFilter', 'itk::AnisotropicFourthOrderLevelSetImageFilter', 'itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('AnisotropicFourthOrderLevelSetImageFilter', 'itk::AnisotropicFourthOrderLevelSetImageFilter', 'itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('CannySegmentationLevelSetImageFilter', 'itk::CannySegmentationLevelSetImageFilter', 'itkCannySegmentationLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('CannySegmentationLevelSetImageFilter', 'itk::CannySegmentationLevelSetImageFilter', 'itkCannySegmentationLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('CollidingFrontsImageFilter', 'itk::CollidingFrontsImageFilter', 'itkCollidingFrontsImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('CollidingFrontsImageFilter', 'itk::CollidingFrontsImageFilter', 'itkCollidingFrontsImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('CurvesLevelSetImageFilter', 'itk::CurvesLevelSetImageFilter', 'itkCurvesLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('CurvesLevelSetImageFilter', 'itk::CurvesLevelSetImageFilter', 'itkCurvesLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('GeodesicActiveContourLevelSetImageFilter', 'itk::GeodesicActiveContourLevelSetImageFilter', 'itkGeodesicActiveContourLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('GeodesicActiveContourLevelSetImageFilter', 'itk::GeodesicActiveContourLevelSetImageFilter', 'itkGeodesicActiveContourLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('GeodesicActiveContourShapePriorLevelSetImageFilter', 'itk::GeodesicActiveContourShapePriorLevelSetImageFilter', 'itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('GeodesicActiveContourShapePriorLevelSetImageFilter', 'itk::GeodesicActiveContourShapePriorLevelSetImageFilter', 'itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('IsotropicFourthOrderLevelSetImageFilter', 'itk::IsotropicFourthOrderLevelSetImageFilter', 'itkIsotropicFourthOrderLevelSetImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('IsotropicFourthOrderLevelSetImageFilter', 'itk::IsotropicFourthOrderLevelSetImageFilter', 'itkIsotropicFourthOrderLevelSetImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('LaplacianSegmentationLevelSetImageFilter', 'itk::LaplacianSegmentationLevelSetImageFilter', 'itkLaplacianSegmentationLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('LaplacianSegmentationLevelSetImageFilter', 'itk::LaplacianSegmentationLevelSetImageFilter', 'itkLaplacianSegmentationLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('NarrowBandCurvesLevelSetImageFilter', 'itk::NarrowBandCurvesLevelSetImageFilter', 'itkNarrowBandCurvesLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('NarrowBandCurvesLevelSetImageFilter', 'itk::NarrowBandCurvesLevelSetImageFilter', 'itkNarrowBandCurvesLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('NarrowBandLevelSetImageFilter', 'itk::NarrowBandLevelSetImageFilter', 'itkNarrowBandLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('NarrowBandLevelSetImageFilter', 'itk::NarrowBandLevelSetImageFilter', 'itkNarrowBandLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('NarrowBandThresholdSegmentationLevelSetImageFilter', 'itk::NarrowBandThresholdSegmentationLevelSetImageFilter', 'itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('NarrowBandThresholdSegmentationLevelSetImageFilter', 'itk::NarrowBandThresholdSegmentationLevelSetImageFilter', 'itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('ParallelSparseFieldLevelSetImageFilter', 'itk::ParallelSparseFieldLevelSetImageFilter', 'itkParallelSparseFieldLevelSetImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ParallelSparseFieldLevelSetImageFilter', 'itk::ParallelSparseFieldLevelSetImageFilter', 'itkParallelSparseFieldLevelSetImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ParallelSparseFieldLevelSetNode', 'itk::ParallelSparseFieldLevelSetNode', 'itkParallelSparseFieldLevelSetNodeI2', False, 'itk::Index< 2 >'),
  ('ParallelSparseFieldLevelSetNode', 'itk::ParallelSparseFieldLevelSetNode', 'itkParallelSparseFieldLevelSetNodeI3', False, 'itk::Index< 3 >'),
  ('SparseFieldLayer', 'itk::SparseFieldLayer', 'itkSparseFieldLayerPSFLSNI2', False, 'itk::ParallelSparseFieldLevelSetNode< itk::Index< 2 > >'),
  ('SparseFieldLayer', 'itk::SparseFieldLayer', 'itkSparseFieldLayerPSFLSNI3', False, 'itk::ParallelSparseFieldLevelSetNode< itk::Index< 3 > >'),
  ('ReinitializeLevelSetImageFilter', 'itk::ReinitializeLevelSetImageFilter', 'itkReinitializeLevelSetImageFilterIF2', True, 'itk::Image< float,2 >'),
  ('ReinitializeLevelSetImageFilter', 'itk::ReinitializeLevelSetImageFilter', 'itkReinitializeLevelSetImageFilterIF3', True, 'itk::Image< float,3 >'),
  ('SegmentationLevelSetFunction', 'itk::SegmentationLevelSetFunction', 'itkSegmentationLevelSetFunctionIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SegmentationLevelSetFunction', 'itk::SegmentationLevelSetFunction', 'itkSegmentationLevelSetFunctionIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ShapeDetectionLevelSetImageFilter', 'itk::ShapeDetectionLevelSetImageFilter', 'itkShapeDetectionLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('ShapeDetectionLevelSetImageFilter', 'itk::ShapeDetectionLevelSetImageFilter', 'itkShapeDetectionLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('ShapePriorMAPCostFunction', 'itk::ShapePriorMAPCostFunction', 'itkShapePriorMAPCostFunctionIF2F', True, 'itk::Image< float,2 >,float'),
  ('ShapePriorMAPCostFunction', 'itk::ShapePriorMAPCostFunction', 'itkShapePriorMAPCostFunctionIF3F', True, 'itk::Image< float,3 >,float'),
  ('ShapePriorMAPCostFunctionBase', 'itk::ShapePriorMAPCostFunctionBase', 'itkShapePriorMAPCostFunctionBaseIF2F', True, 'itk::Image< float,2 >,float'),
  ('ShapePriorMAPCostFunctionBase', 'itk::ShapePriorMAPCostFunctionBase', 'itkShapePriorMAPCostFunctionBaseIF3F', True, 'itk::Image< float,3 >,float'),
  ('ThresholdSegmentationLevelSetImageFilter', 'itk::ThresholdSegmentationLevelSetImageFilter', 'itkThresholdSegmentationLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('ThresholdSegmentationLevelSetImageFilter', 'itk::ThresholdSegmentationLevelSetImageFilter', 'itkThresholdSegmentationLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('UnsharpMaskLevelSetImageFilter', 'itk::UnsharpMaskLevelSetImageFilter', 'itkUnsharpMaskLevelSetImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('UnsharpMaskLevelSetImageFilter', 'itk::UnsharpMaskLevelSetImageFilter', 'itkUnsharpMaskLevelSetImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('VectorThresholdSegmentationLevelSetImageFilter', 'itk::VectorThresholdSegmentationLevelSetImageFilter', 'itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F', True, 'itk::Image< float,2 >,itk::Image< itk::Vector< float,2 >,2 >,float'),
  ('VectorThresholdSegmentationLevelSetImageFilter', 'itk::VectorThresholdSegmentationLevelSetImageFilter', 'itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F', True, 'itk::Image< float,3 >,itk::Image< itk::Vector< float,3 >,3 >,float'),
)
