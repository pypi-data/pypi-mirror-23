depends = ('ITKPyBase', 'ITKStatistics', 'ITKImageFilterBase', 'ITKCommon', )
templates = (
  ('CompositeTransform', 'itk::CompositeTransform', 'itkCompositeTransformD2', True, 'double,2'),
  ('CompositeTransform', 'itk::CompositeTransform', 'itkCompositeTransformD3', True, 'double,3'),
  ('Transform', 'itk::Transform', 'itkTransformD22', True, 'double,2,2'),
  ('Transform', 'itk::Transform', 'itkTransformF22', True, 'float,2,2'),
  ('Transform', 'itk::Transform', 'itkTransformD23', True, 'double,2,3'),
  ('Transform', 'itk::Transform', 'itkTransformF23', True, 'float,2,3'),
  ('Transform', 'itk::Transform', 'itkTransformD32', True, 'double,3,2'),
  ('Transform', 'itk::Transform', 'itkTransformF32', True, 'float,3,2'),
  ('Transform', 'itk::Transform', 'itkTransformD33', True, 'double,3,3'),
  ('Transform', 'itk::Transform', 'itkTransformF33', True, 'float,3,3'),
  ('Transform', 'itk::Transform', 'itkTransformD2', True, 'double,2'),
  ('Transform', 'itk::Transform', 'itkTransformF2', True, 'float,2'),
  ('Transform', 'itk::Transform', 'itkTransformD3', True, 'double,3'),
  ('Transform', 'itk::Transform', 'itkTransformF3', True, 'float,3'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTD22', False, 'itk::Transform< double,2,2 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTF22', False, 'itk::Transform< float,2,2 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTD23', False, 'itk::Transform< double,2,3 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTF23', False, 'itk::Transform< float,2,3 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTD32', False, 'itk::Transform< double,3,2 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTF32', False, 'itk::Transform< float,3,2 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTD33', False, 'itk::Transform< double,3,3 >'),
  ('DataObjectDecorator', 'itk::DataObjectDecorator', 'itkDataObjectDecoratorTF33', False, 'itk::Transform< float,3,3 >'),
  ('TransformBaseTemplate', 'itk::TransformBaseTemplate', 'itkTransformBaseTemplateD', False, 'double'),
  ('TransformBaseTemplate', 'itk::TransformBaseTemplate', 'itkTransformBaseTemplateF', False, 'float'),
  ('MatrixOffsetTransformBase', 'itk::MatrixOffsetTransformBase', 'itkMatrixOffsetTransformBaseD22', True, 'double,2,2'),
  ('MatrixOffsetTransformBase', 'itk::MatrixOffsetTransformBase', 'itkMatrixOffsetTransformBaseF22', True, 'float,2,2'),
  ('MatrixOffsetTransformBase', 'itk::MatrixOffsetTransformBase', 'itkMatrixOffsetTransformBaseD33', True, 'double,3,3'),
  ('MatrixOffsetTransformBase', 'itk::MatrixOffsetTransformBase', 'itkMatrixOffsetTransformBaseF33', True, 'float,3,3'),
  ('Euler2DTransform', 'itk::Euler2DTransform', 'itkEuler2DTransformD', True, 'double'),
  ('Euler3DTransform', 'itk::Euler3DTransform', 'itkEuler3DTransformD', True, 'double'),
  ('MultiTransform', 'itk::MultiTransform', 'itkMultiTransformD22', True, 'double,2,2'),
  ('MultiTransform', 'itk::MultiTransform', 'itkMultiTransformD33', True, 'double,3,3'),
  ('VersorTransform', 'itk::VersorTransform', 'itkVersorTransformD', True, 'double'),
  ('VersorRigid3DTransform', 'itk::VersorRigid3DTransform', 'itkVersorRigid3DTransformD', True, 'double'),
  ('Similarity2DTransform', 'itk::Similarity2DTransform', 'itkSimilarity2DTransformD', True, 'double'),
  ('Similarity3DTransform', 'itk::Similarity3DTransform', 'itkSimilarity3DTransformD', True, 'double'),
  ('AffineTransform', 'itk::AffineTransform', 'itkAffineTransformD2', True, 'double,2'),
  ('AffineTransform', 'itk::AffineTransform', 'itkAffineTransformD3', True, 'double,3'),
  ('ScalableAffineTransform', 'itk::ScalableAffineTransform', 'itkScalableAffineTransformD2', True, 'double,2'),
  ('ScalableAffineTransform', 'itk::ScalableAffineTransform', 'itkScalableAffineTransformD3', True, 'double,3'),
  ('ScaleTransform', 'itk::ScaleTransform', 'itkScaleTransformD2', True, 'double,2'),
  ('ScaleTransform', 'itk::ScaleTransform', 'itkScaleTransformD3', True, 'double,3'),
  ('KernelTransform', 'itk::KernelTransform', 'itkKernelTransformD2', True, 'double,2'),
  ('KernelTransform', 'itk::KernelTransform', 'itkKernelTransformD3', True, 'double,3'),
  ('AzimuthElevationToCartesianTransform', 'itk::AzimuthElevationToCartesianTransform', 'itkAzimuthElevationToCartesianTransformD2', True, 'double,2'),
  ('AzimuthElevationToCartesianTransform', 'itk::AzimuthElevationToCartesianTransform', 'itkAzimuthElevationToCartesianTransformD3', True, 'double,3'),
  ('BSplineBaseTransform', 'itk::BSplineBaseTransform', 'itkBSplineBaseTransformD22', True, 'double,2,2'),
  ('BSplineBaseTransform', 'itk::BSplineBaseTransform', 'itkBSplineBaseTransformD33', True, 'double,3,3'),
  ('BSplineTransform', 'itk::BSplineTransform', 'itkBSplineTransformD22', True, 'double,2,2'),
  ('BSplineTransform', 'itk::BSplineTransform', 'itkBSplineTransformD33', True, 'double,3,3'),
  ('CenteredAffineTransform', 'itk::CenteredAffineTransform', 'itkCenteredAffineTransformD2', True, 'double,2'),
  ('CenteredAffineTransform', 'itk::CenteredAffineTransform', 'itkCenteredAffineTransformD3', True, 'double,3'),
  ('CenteredEuler3DTransform', 'itk::CenteredEuler3DTransform', 'itkCenteredEuler3DTransformD', True, 'double'),
  ('CenteredRigid2DTransform', 'itk::CenteredRigid2DTransform', 'itkCenteredRigid2DTransformD', True, 'double'),
  ('CenteredSimilarity2DTransform', 'itk::CenteredSimilarity2DTransform', 'itkCenteredSimilarity2DTransformD', True, 'double'),
  ('ElasticBodyReciprocalSplineKernelTransform', 'itk::ElasticBodyReciprocalSplineKernelTransform', 'itkElasticBodyReciprocalSplineKernelTransformD2', True, 'double,2'),
  ('ElasticBodyReciprocalSplineKernelTransform', 'itk::ElasticBodyReciprocalSplineKernelTransform', 'itkElasticBodyReciprocalSplineKernelTransformD3', True, 'double,3'),
  ('ElasticBodySplineKernelTransform', 'itk::ElasticBodySplineKernelTransform', 'itkElasticBodySplineKernelTransformD2', True, 'double,2'),
  ('ElasticBodySplineKernelTransform', 'itk::ElasticBodySplineKernelTransform', 'itkElasticBodySplineKernelTransformD3', True, 'double,3'),
  ('FixedCenterOfRotationAffineTransform', 'itk::FixedCenterOfRotationAffineTransform', 'itkFixedCenterOfRotationAffineTransformD2', True, 'double,2'),
  ('FixedCenterOfRotationAffineTransform', 'itk::FixedCenterOfRotationAffineTransform', 'itkFixedCenterOfRotationAffineTransformD3', True, 'double,3'),
  ('IdentityTransform', 'itk::IdentityTransform', 'itkIdentityTransformD2', True, 'double,2'),
  ('IdentityTransform', 'itk::IdentityTransform', 'itkIdentityTransformD3', True, 'double,3'),
  ('QuaternionRigidTransform', 'itk::QuaternionRigidTransform', 'itkQuaternionRigidTransformD', True, 'double'),
  ('Rigid2DTransform', 'itk::Rigid2DTransform', 'itkRigid2DTransformD', True, 'double'),
  ('Rigid3DPerspectiveTransform', 'itk::Rigid3DPerspectiveTransform', 'itkRigid3DPerspectiveTransformD', True, 'double'),
  ('Rigid3DTransform', 'itk::Rigid3DTransform', 'itkRigid3DTransformD', True, 'double'),
  ('ScaleLogarithmicTransform', 'itk::ScaleLogarithmicTransform', 'itkScaleLogarithmicTransformD2', True, 'double,2'),
  ('ScaleLogarithmicTransform', 'itk::ScaleLogarithmicTransform', 'itkScaleLogarithmicTransformD3', True, 'double,3'),
  ('ScaleSkewVersor3DTransform', 'itk::ScaleSkewVersor3DTransform', 'itkScaleSkewVersor3DTransformD', True, 'double'),
  ('ScaleVersor3DTransform', 'itk::ScaleVersor3DTransform', 'itkScaleVersor3DTransformD', True, 'double'),
  ('ThinPlateR2LogRSplineKernelTransform', 'itk::ThinPlateR2LogRSplineKernelTransform', 'itkThinPlateR2LogRSplineKernelTransformD2', True, 'double,2'),
  ('ThinPlateR2LogRSplineKernelTransform', 'itk::ThinPlateR2LogRSplineKernelTransform', 'itkThinPlateR2LogRSplineKernelTransformD3', True, 'double,3'),
  ('ThinPlateSplineKernelTransform', 'itk::ThinPlateSplineKernelTransform', 'itkThinPlateSplineKernelTransformD2', True, 'double,2'),
  ('ThinPlateSplineKernelTransform', 'itk::ThinPlateSplineKernelTransform', 'itkThinPlateSplineKernelTransformD3', True, 'double,3'),
  ('TranslationTransform', 'itk::TranslationTransform', 'itkTranslationTransformD2', True, 'double,2'),
  ('TranslationTransform', 'itk::TranslationTransform', 'itkTranslationTransformD3', True, 'double,3'),
  ('VolumeSplineKernelTransform', 'itk::VolumeSplineKernelTransform', 'itkVolumeSplineKernelTransformD2', True, 'double,2'),
  ('VolumeSplineKernelTransform', 'itk::VolumeSplineKernelTransform', 'itkVolumeSplineKernelTransformD3', True, 'double,3'),
)
