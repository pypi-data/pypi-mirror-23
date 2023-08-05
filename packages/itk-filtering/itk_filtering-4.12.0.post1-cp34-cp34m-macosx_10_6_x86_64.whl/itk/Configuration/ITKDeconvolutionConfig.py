depends = ('ITKPyBase', 'ITKImageSources', 'ITKConvolution', )
templates = (
  ('IterativeDeconvolutionImageFilter', 'itk::IterativeDeconvolutionImageFilter', 'itkIterativeDeconvolutionImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('IterativeDeconvolutionImageFilter', 'itk::IterativeDeconvolutionImageFilter', 'itkIterativeDeconvolutionImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('IterativeDeconvolutionImageFilter', 'itk::IterativeDeconvolutionImageFilter', 'itkIterativeDeconvolutionImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('IterativeDeconvolutionImageFilter', 'itk::IterativeDeconvolutionImageFilter', 'itkIterativeDeconvolutionImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('IterativeDeconvolutionImageFilter', 'itk::IterativeDeconvolutionImageFilter', 'itkIterativeDeconvolutionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('IterativeDeconvolutionImageFilter', 'itk::IterativeDeconvolutionImageFilter', 'itkIterativeDeconvolutionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('InverseDeconvolutionImageFilter', 'itk::InverseDeconvolutionImageFilter', 'itkInverseDeconvolutionImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('InverseDeconvolutionImageFilter', 'itk::InverseDeconvolutionImageFilter', 'itkInverseDeconvolutionImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('InverseDeconvolutionImageFilter', 'itk::InverseDeconvolutionImageFilter', 'itkInverseDeconvolutionImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('InverseDeconvolutionImageFilter', 'itk::InverseDeconvolutionImageFilter', 'itkInverseDeconvolutionImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('InverseDeconvolutionImageFilter', 'itk::InverseDeconvolutionImageFilter', 'itkInverseDeconvolutionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('InverseDeconvolutionImageFilter', 'itk::InverseDeconvolutionImageFilter', 'itkInverseDeconvolutionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('LandweberDeconvolutionImageFilter', 'itk::LandweberDeconvolutionImageFilter', 'itkLandweberDeconvolutionImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('LandweberDeconvolutionImageFilter', 'itk::LandweberDeconvolutionImageFilter', 'itkLandweberDeconvolutionImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('LandweberDeconvolutionImageFilter', 'itk::LandweberDeconvolutionImageFilter', 'itkLandweberDeconvolutionImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('LandweberDeconvolutionImageFilter', 'itk::LandweberDeconvolutionImageFilter', 'itkLandweberDeconvolutionImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('LandweberDeconvolutionImageFilter', 'itk::LandweberDeconvolutionImageFilter', 'itkLandweberDeconvolutionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('LandweberDeconvolutionImageFilter', 'itk::LandweberDeconvolutionImageFilter', 'itkLandweberDeconvolutionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ProjectedLandweberDeconvolutionImageFilter', 'itk::ProjectedLandweberDeconvolutionImageFilter', 'itkProjectedLandweberDeconvolutionImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('ProjectedLandweberDeconvolutionImageFilter', 'itk::ProjectedLandweberDeconvolutionImageFilter', 'itkProjectedLandweberDeconvolutionImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('ProjectedLandweberDeconvolutionImageFilter', 'itk::ProjectedLandweberDeconvolutionImageFilter', 'itkProjectedLandweberDeconvolutionImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('ProjectedLandweberDeconvolutionImageFilter', 'itk::ProjectedLandweberDeconvolutionImageFilter', 'itkProjectedLandweberDeconvolutionImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('ProjectedLandweberDeconvolutionImageFilter', 'itk::ProjectedLandweberDeconvolutionImageFilter', 'itkProjectedLandweberDeconvolutionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ProjectedLandweberDeconvolutionImageFilter', 'itk::ProjectedLandweberDeconvolutionImageFilter', 'itkProjectedLandweberDeconvolutionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('RichardsonLucyDeconvolutionImageFilter', 'itk::RichardsonLucyDeconvolutionImageFilter', 'itkRichardsonLucyDeconvolutionImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('RichardsonLucyDeconvolutionImageFilter', 'itk::RichardsonLucyDeconvolutionImageFilter', 'itkRichardsonLucyDeconvolutionImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('RichardsonLucyDeconvolutionImageFilter', 'itk::RichardsonLucyDeconvolutionImageFilter', 'itkRichardsonLucyDeconvolutionImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('RichardsonLucyDeconvolutionImageFilter', 'itk::RichardsonLucyDeconvolutionImageFilter', 'itkRichardsonLucyDeconvolutionImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('RichardsonLucyDeconvolutionImageFilter', 'itk::RichardsonLucyDeconvolutionImageFilter', 'itkRichardsonLucyDeconvolutionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('RichardsonLucyDeconvolutionImageFilter', 'itk::RichardsonLucyDeconvolutionImageFilter', 'itkRichardsonLucyDeconvolutionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('TikhonovDeconvolutionImageFilter', 'itk::TikhonovDeconvolutionImageFilter', 'itkTikhonovDeconvolutionImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('TikhonovDeconvolutionImageFilter', 'itk::TikhonovDeconvolutionImageFilter', 'itkTikhonovDeconvolutionImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('TikhonovDeconvolutionImageFilter', 'itk::TikhonovDeconvolutionImageFilter', 'itkTikhonovDeconvolutionImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('TikhonovDeconvolutionImageFilter', 'itk::TikhonovDeconvolutionImageFilter', 'itkTikhonovDeconvolutionImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('TikhonovDeconvolutionImageFilter', 'itk::TikhonovDeconvolutionImageFilter', 'itkTikhonovDeconvolutionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('TikhonovDeconvolutionImageFilter', 'itk::TikhonovDeconvolutionImageFilter', 'itkTikhonovDeconvolutionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('WienerDeconvolutionImageFilter', 'itk::WienerDeconvolutionImageFilter', 'itkWienerDeconvolutionImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('WienerDeconvolutionImageFilter', 'itk::WienerDeconvolutionImageFilter', 'itkWienerDeconvolutionImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('WienerDeconvolutionImageFilter', 'itk::WienerDeconvolutionImageFilter', 'itkWienerDeconvolutionImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('WienerDeconvolutionImageFilter', 'itk::WienerDeconvolutionImageFilter', 'itkWienerDeconvolutionImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('WienerDeconvolutionImageFilter', 'itk::WienerDeconvolutionImageFilter', 'itkWienerDeconvolutionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('WienerDeconvolutionImageFilter', 'itk::WienerDeconvolutionImageFilter', 'itkWienerDeconvolutionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
)
