# coding=gbk
try:
    from osgeo import gdal
    from osgeo import ogr
except ImportError:
    import gdal
    import ogr
# pathStr,shp�ļ���ȫ·��
def ReadVectorFile(pathStr):

    # ���ؽ����һ��list
    result=[]
    # ֧������·��
    gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "NO")
    # ���Ա��ֶ�֧������
    gdal.SetConfigOption("SHAPE_ENCODING", "")
    strVectorFile = pathStr
    # ע�����е�����
    ogr.RegisterAll()
    # ������
    ds = ogr.Open(strVectorFile, 0)
    # ��ȡ������Դ�е�ͼ�������һ��shp����ͼ��ֻ��һ���������mdb��dxf��ͼ��ͻ��ж��
    iLayerCount = ds.GetLayerCount()
    # ��ȡ��һ��ͼ��
    oLayer = ds.GetLayerByIndex(0)
    # ��ͼ����г�ʼ��
    oLayer.ResetReading()
    # ��ȡͼ���е����Ա��ͷ�����,���Զ��彨�����
    print("���Ա�ṹ��Ϣ��")
    oDefn = oLayer.GetLayerDefn()
    iFieldCount = oDefn.GetFieldCount()
    for iAttr in range(iFieldCount):
        oField = oDefn.GetFieldDefn(iAttr)
        print("%s: %s(%d.%d)" % ( \
     \
            oField.GetNameRef(), \
     \
            oField.GetFieldTypeName(oField.GetType()), \
     \
            oField.GetWidth(), \
     \
            oField.GetPrecision()))
    # ���ͼ���е�Ҫ�ظ���
    print("Ҫ�ظ��� = ", oLayer.GetFeatureCount(0))
    oFeature = oLayer.GetNextFeature()
    # ���濪ʼ����ͼ���е�Ҫ�أ���������Ϊstring���
    while oFeature is not None:
        # ��ȡҪ���е����Ա�����
        lineStr=[]
        for iField in range(iFieldCount):
            lineStr.append(oFeature.GetFieldAsString(iField))
    # ��ȡҪ���еļ�����
        oGeometry = oFeature.GetGeometryRef()
        lineStr.append(str(oGeometry))
        # print(lineStr)
        result.append(lineStr)
        # ѭ��
        oFeature = oLayer.GetNextFeature()
    print("���ݼ��رգ�")
    return result

if __name__ == '__main__':
    result=ReadVectorFile(r'D:\gismap\data\v6_time_pref_pgn_utf_wgs84\v6_time_pref_pgn_utf_wgs84.shp')
    f_new=open(r'D:\gismap\data\v6_time_pref_pgn_utf_wgs84\v6_time_pref_pgn_utf_wgs84.txt','a',encoding='utf-8')
    for r in result:
        for p in r:
            f_new.write(p+'\t')
        f_new.write('\n')
    f_new.close()
