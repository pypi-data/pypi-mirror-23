depends = ('ITKPyBase', 'ITKTransform', 'ITKStatistics', )
templates = (
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionISS2DF', True, 'itk::Image< signed short,2 >,double,float'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionISS2DD', True, 'itk::Image< signed short,2 >,double,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIUC2DF', True, 'itk::Image< unsigned char,2 >,double,float'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIUC2DD', True, 'itk::Image< unsigned char,2 >,double,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIF2DF', True, 'itk::Image< float,2 >,double,float'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIF2DD', True, 'itk::Image< float,2 >,double,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIVF22VD2D', True, 'itk::Image< itk::Vector< float,2 >,2 >,itk::Vector< double,2 >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIVF22CVD2D', True, 'itk::Image< itk::Vector< float,2 >,2 >,itk::CovariantVector< double,2 >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIVF22DD', True, 'itk::Image< itk::Vector< float,2 >,2 >,double,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionICVF22VD2D', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >,itk::Vector< double,2 >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionICVF22CVD2D', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >,itk::CovariantVector< double,2 >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionICVF22DD', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >,double,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIRGBUC2RGBUCD', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >,itk::RGBPixel< unsigned char >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIRGBAUC2RGBAUCD', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >,itk::RGBAPixel< unsigned char >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIRGBUC2RGBDD', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >,itk::RGBPixel< double >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIRGBAUC2RGBADD', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >,itk::RGBAPixel< double >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionISS3DF', True, 'itk::Image< signed short,3 >,double,float'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionISS3DD', True, 'itk::Image< signed short,3 >,double,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIUC3DF', True, 'itk::Image< unsigned char,3 >,double,float'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIUC3DD', True, 'itk::Image< unsigned char,3 >,double,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIF3DF', True, 'itk::Image< float,3 >,double,float'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIF3DD', True, 'itk::Image< float,3 >,double,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIVF33VD3D', True, 'itk::Image< itk::Vector< float,3 >,3 >,itk::Vector< double,3 >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIVF33CVD3D', True, 'itk::Image< itk::Vector< float,3 >,3 >,itk::CovariantVector< double,3 >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIVF33DD', True, 'itk::Image< itk::Vector< float,3 >,3 >,double,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionICVF33VD3D', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >,itk::Vector< double,3 >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionICVF33CVD3D', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >,itk::CovariantVector< double,3 >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionICVF33DD', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >,double,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIRGBUC3RGBUCD', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >,itk::RGBPixel< unsigned char >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIRGBAUC3RGBAUCD', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >,itk::RGBAPixel< unsigned char >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIRGBUC3RGBDD', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >,itk::RGBPixel< double >,double'),
  ('ImageFunction', 'itk::ImageFunction', 'itkImageFunctionIRGBAUC3RGBADD', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >,itk::RGBAPixel< double >,double'),
  ('BSplineDecompositionImageFilter', 'itk::BSplineDecompositionImageFilter', 'itkBSplineDecompositionImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('BSplineDecompositionImageFilter', 'itk::BSplineDecompositionImageFilter', 'itkBSplineDecompositionImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('BSplineDecompositionImageFilter', 'itk::BSplineDecompositionImageFilter', 'itkBSplineDecompositionImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('BSplineDecompositionImageFilter', 'itk::BSplineDecompositionImageFilter', 'itkBSplineDecompositionImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('BSplineDecompositionImageFilter', 'itk::BSplineDecompositionImageFilter', 'itkBSplineDecompositionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('BSplineDecompositionImageFilter', 'itk::BSplineDecompositionImageFilter', 'itkBSplineDecompositionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('BSplineInterpolateImageFunction', 'itk::BSplineInterpolateImageFunction', 'itkBSplineInterpolateImageFunctionISS2DSS', True, 'itk::Image< signed short,2 >,double,signed short'),
  ('BSplineInterpolateImageFunction', 'itk::BSplineInterpolateImageFunction', 'itkBSplineInterpolateImageFunctionIUC2DUC', True, 'itk::Image< unsigned char,2 >,double,unsigned char'),
  ('BSplineInterpolateImageFunction', 'itk::BSplineInterpolateImageFunction', 'itkBSplineInterpolateImageFunctionIF2DF', True, 'itk::Image< float,2 >,double,float'),
  ('BSplineInterpolateImageFunction', 'itk::BSplineInterpolateImageFunction', 'itkBSplineInterpolateImageFunctionISS3DSS', True, 'itk::Image< signed short,3 >,double,signed short'),
  ('BSplineInterpolateImageFunction', 'itk::BSplineInterpolateImageFunction', 'itkBSplineInterpolateImageFunctionIUC3DUC', True, 'itk::Image< unsigned char,3 >,double,unsigned char'),
  ('BSplineInterpolateImageFunction', 'itk::BSplineInterpolateImageFunction', 'itkBSplineInterpolateImageFunctionIF3DF', True, 'itk::Image< float,3 >,double,float'),
  ('BSplineResampleImageFunction', 'itk::BSplineResampleImageFunction', 'itkBSplineResampleImageFunctionISS2D', True, 'itk::Image< signed short,2 >,double'),
  ('BSplineResampleImageFunction', 'itk::BSplineResampleImageFunction', 'itkBSplineResampleImageFunctionIUC2D', True, 'itk::Image< unsigned char,2 >,double'),
  ('BSplineResampleImageFunction', 'itk::BSplineResampleImageFunction', 'itkBSplineResampleImageFunctionIF2D', True, 'itk::Image< float,2 >,double'),
  ('BSplineResampleImageFunction', 'itk::BSplineResampleImageFunction', 'itkBSplineResampleImageFunctionISS3D', True, 'itk::Image< signed short,3 >,double'),
  ('BSplineResampleImageFunction', 'itk::BSplineResampleImageFunction', 'itkBSplineResampleImageFunctionIUC3D', True, 'itk::Image< unsigned char,3 >,double'),
  ('BSplineResampleImageFunction', 'itk::BSplineResampleImageFunction', 'itkBSplineResampleImageFunctionIF3D', True, 'itk::Image< float,3 >,double'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionISS2D', True, 'itk::Image< signed short,2 >,double'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionISS2F', True, 'itk::Image< signed short,2 >,float'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionIUC2D', True, 'itk::Image< unsigned char,2 >,double'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionIUC2F', True, 'itk::Image< unsigned char,2 >,float'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionIF2D', True, 'itk::Image< float,2 >,double'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionIF2F', True, 'itk::Image< float,2 >,float'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionIVF22D', True, 'itk::Image< itk::Vector< float,2 >,2 >,double'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionICVF22D', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >,double'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionIRGBUC2D', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >,double'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionIRGBAUC2D', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >,double'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionISS3D', True, 'itk::Image< signed short,3 >,double'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionISS3F', True, 'itk::Image< signed short,3 >,float'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionIUC3D', True, 'itk::Image< unsigned char,3 >,double'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionIUC3F', True, 'itk::Image< unsigned char,3 >,float'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionIF3D', True, 'itk::Image< float,3 >,double'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionIF3F', True, 'itk::Image< float,3 >,float'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionIVF33D', True, 'itk::Image< itk::Vector< float,3 >,3 >,double'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionICVF33D', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >,double'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionIRGBUC3D', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >,double'),
  ('InterpolateImageFunction', 'itk::InterpolateImageFunction', 'itkInterpolateImageFunctionIRGBAUC3D', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >,double'),
  ('LinearInterpolateImageFunction', 'itk::LinearInterpolateImageFunction', 'itkLinearInterpolateImageFunctionISS2D', True, 'itk::Image< signed short,2 >,double'),
  ('LinearInterpolateImageFunction', 'itk::LinearInterpolateImageFunction', 'itkLinearInterpolateImageFunctionIUC2D', True, 'itk::Image< unsigned char,2 >,double'),
  ('LinearInterpolateImageFunction', 'itk::LinearInterpolateImageFunction', 'itkLinearInterpolateImageFunctionIF2D', True, 'itk::Image< float,2 >,double'),
  ('LinearInterpolateImageFunction', 'itk::LinearInterpolateImageFunction', 'itkLinearInterpolateImageFunctionIVF22D', True, 'itk::Image< itk::Vector< float,2 >,2 >,double'),
  ('LinearInterpolateImageFunction', 'itk::LinearInterpolateImageFunction', 'itkLinearInterpolateImageFunctionICVF22D', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >,double'),
  ('LinearInterpolateImageFunction', 'itk::LinearInterpolateImageFunction', 'itkLinearInterpolateImageFunctionIRGBUC2D', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >,double'),
  ('LinearInterpolateImageFunction', 'itk::LinearInterpolateImageFunction', 'itkLinearInterpolateImageFunctionIRGBAUC2D', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >,double'),
  ('LinearInterpolateImageFunction', 'itk::LinearInterpolateImageFunction', 'itkLinearInterpolateImageFunctionISS3D', True, 'itk::Image< signed short,3 >,double'),
  ('LinearInterpolateImageFunction', 'itk::LinearInterpolateImageFunction', 'itkLinearInterpolateImageFunctionIUC3D', True, 'itk::Image< unsigned char,3 >,double'),
  ('LinearInterpolateImageFunction', 'itk::LinearInterpolateImageFunction', 'itkLinearInterpolateImageFunctionIF3D', True, 'itk::Image< float,3 >,double'),
  ('LinearInterpolateImageFunction', 'itk::LinearInterpolateImageFunction', 'itkLinearInterpolateImageFunctionIVF33D', True, 'itk::Image< itk::Vector< float,3 >,3 >,double'),
  ('LinearInterpolateImageFunction', 'itk::LinearInterpolateImageFunction', 'itkLinearInterpolateImageFunctionICVF33D', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >,double'),
  ('LinearInterpolateImageFunction', 'itk::LinearInterpolateImageFunction', 'itkLinearInterpolateImageFunctionIRGBUC3D', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >,double'),
  ('LinearInterpolateImageFunction', 'itk::LinearInterpolateImageFunction', 'itkLinearInterpolateImageFunctionIRGBAUC3D', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >,double'),
  ('NearestNeighborInterpolateImageFunction', 'itk::NearestNeighborInterpolateImageFunction', 'itkNearestNeighborInterpolateImageFunctionISS2D', True, 'itk::Image< signed short,2 >,double'),
  ('NearestNeighborInterpolateImageFunction', 'itk::NearestNeighborInterpolateImageFunction', 'itkNearestNeighborInterpolateImageFunctionIUC2D', True, 'itk::Image< unsigned char,2 >,double'),
  ('NearestNeighborInterpolateImageFunction', 'itk::NearestNeighborInterpolateImageFunction', 'itkNearestNeighborInterpolateImageFunctionIF2D', True, 'itk::Image< float,2 >,double'),
  ('NearestNeighborInterpolateImageFunction', 'itk::NearestNeighborInterpolateImageFunction', 'itkNearestNeighborInterpolateImageFunctionISS3D', True, 'itk::Image< signed short,3 >,double'),
  ('NearestNeighborInterpolateImageFunction', 'itk::NearestNeighborInterpolateImageFunction', 'itkNearestNeighborInterpolateImageFunctionIUC3D', True, 'itk::Image< unsigned char,3 >,double'),
  ('NearestNeighborInterpolateImageFunction', 'itk::NearestNeighborInterpolateImageFunction', 'itkNearestNeighborInterpolateImageFunctionIF3D', True, 'itk::Image< float,3 >,double'),
  ('RayCastInterpolateImageFunction', 'itk::RayCastInterpolateImageFunction', 'itkRayCastInterpolateImageFunctionISS3D', True, 'itk::Image< signed short,3 >,double'),
  ('RayCastInterpolateImageFunction', 'itk::RayCastInterpolateImageFunction', 'itkRayCastInterpolateImageFunctionISS3F', True, 'itk::Image< signed short,3 >,float'),
  ('RayCastInterpolateImageFunction', 'itk::RayCastInterpolateImageFunction', 'itkRayCastInterpolateImageFunctionIUC3D', True, 'itk::Image< unsigned char,3 >,double'),
  ('RayCastInterpolateImageFunction', 'itk::RayCastInterpolateImageFunction', 'itkRayCastInterpolateImageFunctionIUC3F', True, 'itk::Image< unsigned char,3 >,float'),
  ('RayCastInterpolateImageFunction', 'itk::RayCastInterpolateImageFunction', 'itkRayCastInterpolateImageFunctionIF3D', True, 'itk::Image< float,3 >,double'),
  ('RayCastInterpolateImageFunction', 'itk::RayCastInterpolateImageFunction', 'itkRayCastInterpolateImageFunctionIF3F', True, 'itk::Image< float,3 >,float'),
)
