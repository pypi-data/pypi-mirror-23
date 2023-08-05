depends = ('ITKPyBase', 'ITKQuadEdgeMesh', 'ITKMesh', 'ITKConnectedComponents', )
templates = (
  ('LevelSetNode', 'itk::LevelSetNode', 'itkLevelSetNodeSS2', True, 'signed short,2'),
  ('LevelSetNode', 'itk::LevelSetNode', 'itkLevelSetNodeUC2', True, 'unsigned char,2'),
  ('LevelSetNode', 'itk::LevelSetNode', 'itkLevelSetNodeF2', True, 'float,2'),
  ('LevelSetNode', 'itk::LevelSetNode', 'itkLevelSetNodeSS3', True, 'signed short,3'),
  ('LevelSetNode', 'itk::LevelSetNode', 'itkLevelSetNodeUC3', True, 'unsigned char,3'),
  ('LevelSetNode', 'itk::LevelSetNode', 'itkLevelSetNodeF3', True, 'float,3'),
  ('NodePair', 'itk::NodePair', 'itkNodePairI2SS', True, 'itk::Index<2>, signed short'),
  ('NodePair', 'itk::NodePair', 'itkNodePairI2UC', True, 'itk::Index<2>, unsigned char'),
  ('NodePair', 'itk::NodePair', 'itkNodePairI2F', True, 'itk::Index<2>, float'),
  ('NodePair', 'itk::NodePair', 'itkNodePairI3SS', True, 'itk::Index<3>, signed short'),
  ('NodePair', 'itk::NodePair', 'itkNodePairI3UC', True, 'itk::Index<3>, unsigned char'),
  ('NodePair', 'itk::NodePair', 'itkNodePairI3F', True, 'itk::Index<3>, float'),
  ('FastMarchingStoppingCriterionBase', 'itk::FastMarchingStoppingCriterionBase', 'itkFastMarchingStoppingCriterionBaseIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('FastMarchingStoppingCriterionBase', 'itk::FastMarchingStoppingCriterionBase', 'itkFastMarchingStoppingCriterionBaseIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('VectorContainer', 'itk::VectorContainer', 'itkVectorContainerUILSNSS2', False, 'unsigned int,itk::LevelSetNode< signed short,2 >'),
  ('VectorContainer', 'itk::VectorContainer', 'itkVectorContainerULNPI2SS', False, 'unsigned long, itk::NodePair< itk::Index<2>, signed short >'),
  ('VectorContainer', 'itk::VectorContainer', 'itkVectorContainerUILSNUC2', False, 'unsigned int,itk::LevelSetNode< unsigned char,2 >'),
  ('VectorContainer', 'itk::VectorContainer', 'itkVectorContainerULNPI2UC', False, 'unsigned long, itk::NodePair< itk::Index<2>, unsigned char >'),
  ('VectorContainer', 'itk::VectorContainer', 'itkVectorContainerUILSNF2', False, 'unsigned int,itk::LevelSetNode< float,2 >'),
  ('VectorContainer', 'itk::VectorContainer', 'itkVectorContainerULNPI2F', False, 'unsigned long, itk::NodePair< itk::Index<2>, float >'),
  ('VectorContainer', 'itk::VectorContainer', 'itkVectorContainerUILSNSS3', False, 'unsigned int,itk::LevelSetNode< signed short,3 >'),
  ('VectorContainer', 'itk::VectorContainer', 'itkVectorContainerULNPI3SS', False, 'unsigned long, itk::NodePair< itk::Index<3>, signed short >'),
  ('VectorContainer', 'itk::VectorContainer', 'itkVectorContainerUILSNUC3', False, 'unsigned int,itk::LevelSetNode< unsigned char,3 >'),
  ('VectorContainer', 'itk::VectorContainer', 'itkVectorContainerULNPI3UC', False, 'unsigned long, itk::NodePair< itk::Index<3>, unsigned char >'),
  ('VectorContainer', 'itk::VectorContainer', 'itkVectorContainerUILSNF3', False, 'unsigned int,itk::LevelSetNode< float,3 >'),
  ('VectorContainer', 'itk::VectorContainer', 'itkVectorContainerULNPI3F', False, 'unsigned long, itk::NodePair< itk::Index<3>, float >'),
  ('FastMarchingBase', 'itk::FastMarchingBase', 'itkFastMarchingBaseIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('FastMarchingBase', 'itk::FastMarchingBase', 'itkFastMarchingBaseIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('FastMarchingImageFilterBase', 'itk::FastMarchingImageFilterBase', 'itkFastMarchingImageFilterBaseIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('FastMarchingImageFilterBase', 'itk::FastMarchingImageFilterBase', 'itkFastMarchingImageFilterBaseIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('FastMarchingExtensionImageFilter', 'itk::FastMarchingExtensionImageFilter', 'itkFastMarchingExtensionImageFilterIF2UC1IF2', True, 'itk::Image< float,2 >, unsigned char, 1, itk::Image< float,2 >'),
  ('FastMarchingExtensionImageFilter', 'itk::FastMarchingExtensionImageFilter', 'itkFastMarchingExtensionImageFilterIF3UC1IF3', True, 'itk::Image< float,3 >, unsigned char, 1, itk::Image< float,3 >'),
  ('FastMarchingImageFilter', 'itk::FastMarchingImageFilter', 'itkFastMarchingImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('FastMarchingImageFilter', 'itk::FastMarchingImageFilter', 'itkFastMarchingImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('FastMarchingImageToNodePairContainerAdaptor', 'itk::FastMarchingImageToNodePairContainerAdaptor', 'itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >, itk::Image< float,2 >'),
  ('FastMarchingImageToNodePairContainerAdaptor', 'itk::FastMarchingImageToNodePairContainerAdaptor', 'itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >, itk::Image< float,3 >'),
  ('FastMarchingReachedTargetNodesStoppingCriterion', 'itk::FastMarchingReachedTargetNodesStoppingCriterion', 'itkFastMarchingReachedTargetNodesStoppingCriterionIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('FastMarchingReachedTargetNodesStoppingCriterion', 'itk::FastMarchingReachedTargetNodesStoppingCriterion', 'itkFastMarchingReachedTargetNodesStoppingCriterionIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('FastMarchingThresholdStoppingCriterion', 'itk::FastMarchingThresholdStoppingCriterion', 'itkFastMarchingThresholdStoppingCriterionIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('FastMarchingThresholdStoppingCriterion', 'itk::FastMarchingThresholdStoppingCriterion', 'itkFastMarchingThresholdStoppingCriterionIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('FastMarchingUpwindGradientImageFilter', 'itk::FastMarchingUpwindGradientImageFilter', 'itkFastMarchingUpwindGradientImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('FastMarchingUpwindGradientImageFilter', 'itk::FastMarchingUpwindGradientImageFilter', 'itkFastMarchingUpwindGradientImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('FastMarchingUpwindGradientImageFilterBase', 'itk::FastMarchingUpwindGradientImageFilterBase', 'itkFastMarchingUpwindGradientImageFilterBaseIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('FastMarchingUpwindGradientImageFilterBase', 'itk::FastMarchingUpwindGradientImageFilterBase', 'itkFastMarchingUpwindGradientImageFilterBaseIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
)
