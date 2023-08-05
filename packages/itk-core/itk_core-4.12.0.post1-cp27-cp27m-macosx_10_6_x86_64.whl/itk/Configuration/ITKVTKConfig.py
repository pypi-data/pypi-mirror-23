depends = ('ITKPyBase', 'ITKCommon', )
templates = (
  ('VTKImageExportBase', 'itk::VTKImageExportBase', 'itkVTKImageExportBase', True),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIUL2', True, 'itk::Image< unsigned long,2 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIUL3', True, 'itk::Image< unsigned long,3 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportISS2', True, 'itk::Image< signed short,2 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportISS3', True, 'itk::Image< signed short,3 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIF2', True, 'itk::Image< float,2 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIF3', True, 'itk::Image< float,3 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIRGBUC2', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIRGBUC3', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIRGBAUC2', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIRGBAUC3', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIVF22', True, 'itk::Image< itk::Vector< float,2 >,2 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIVF23', True, 'itk::Image< itk::Vector< float,2 >,3 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIVF32', True, 'itk::Image< itk::Vector< float,3 >,2 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIVF33', True, 'itk::Image< itk::Vector< float,3 >,3 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIVF42', True, 'itk::Image< itk::Vector< float,4 >,2 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportIVF43', True, 'itk::Image< itk::Vector< float,4 >,3 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportICVF22', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportICVF23', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportICVF32', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportICVF33', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportICVF42', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('VTKImageExport', 'itk::VTKImageExport', 'itkVTKImageExportICVF43', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIUL2', True, 'itk::Image< unsigned long,2 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIUL3', True, 'itk::Image< unsigned long,3 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportISS2', True, 'itk::Image< signed short,2 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportISS3', True, 'itk::Image< signed short,3 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIF2', True, 'itk::Image< float,2 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIF3', True, 'itk::Image< float,3 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIRGBUC2', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIRGBUC3', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIRGBAUC2', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIRGBAUC3', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIVF22', True, 'itk::Image< itk::Vector< float,2 >,2 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIVF23', True, 'itk::Image< itk::Vector< float,2 >,3 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIVF32', True, 'itk::Image< itk::Vector< float,3 >,2 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIVF33', True, 'itk::Image< itk::Vector< float,3 >,3 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIVF42', True, 'itk::Image< itk::Vector< float,4 >,2 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportIVF43', True, 'itk::Image< itk::Vector< float,4 >,3 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportICVF22', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportICVF23', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportICVF32', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportICVF33', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportICVF42', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('VTKImageImport', 'itk::VTKImageImport', 'itkVTKImageImportICVF43', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >'),
)
