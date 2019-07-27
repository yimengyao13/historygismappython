# coding=gbk
import psycopg2
# �������ݿ�
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")
print('���ӳɹ�')
# �����α�
cur = conn.cursor()
# ����
cur.execute('''--����
CREATE TABLE public. v6_time_pref_pts_utf_wgs84(
  gid SERIAL8 PRIMARY KEY NOT NULL,
  name_py varchar(40),
  name_ch varchar(45),
  name_ft varchar(45),
  x_coor float8,
  y_coor float8,
  pres_loc varchar(60),
  type_py varchar(15),
  type_ch varchar(15),
  lev_rank varchar(1),
  beg_yr int8,
  beg_rule varchar(1),
  end_yr int8,
  end_rule varchar(1),
  note_id int8,
  obj_type varchar(7),
  sys_id int8,
  geo_src varchar(10),
  compiler varchar(12),
  gecomplr varchar(10),
  checker varchar(10),
  ent_date varchar(10),
  beg_chg_ty varchar(21),
  end_chg_ty varchar(30),
  geom geometry
);
--��������
CREATE INDEX v6_time_pref_pts_utf_wgs84_index ON v6_time_pref_pts_utf_wgs84 USING btree(gid);
--��˵��
COMMENT ON TABLE public.v6_time_pref_pts_utf_wgs84 IS '��6���й���ʷ����ʱ�����е�����';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.gid IS '����ID';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.name_py IS 'ƴ������';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.name_ch IS '������������';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.name_ft IS '������������';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.x_coor IS '����';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.y_coor IS 'γ��';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.pres_loc IS '�����ڵ�';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.type_py IS '��������ƴ��';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.type_ch IS '�������ͼ�������';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.lev_rank IS '���Ƶȼ�';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.beg_yr IS '���ƿ�ʼʱ��';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.beg_rule IS '��ʼʱ�侫��';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.end_yr IS '���ƽ���ʱ��';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.end_rule IS '����ʱ�侫��';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.note_id IS 'ϵͳid';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.obj_type IS 'geometry��������';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.sys_id IS 'ϵͳid';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.geo_src IS 'geometry������Դ';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.compiler IS '�༭��Ա';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.gecomplr IS '������Ա';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.checker IS '�����Ա';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.ent_date IS '����ʱ��';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.beg_chg_ty IS '���ƿ�ʼԭ��';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.end_chg_ty IS '���ƽ���ԭ��';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84.geom IS 'geometry����';''')
# ��������
f=open(r'D:\gismap\data\v6_time_pref_pts_utf_wgs84\v6_time_pref_pts_utf_wgs84.txt','r',encoding='utf-8')
# ���ж���txt
flines=f.readlines()
for line in flines:
    # ȥ�����ţ��д�
    abbrlist=line.replace("'"," ").split('\t')
    # name_py,name_ch,name_ft,x_coor,y_coor,pres_loc,type_py,type_ch,lev_rank,beg_yr,beg_rule,end_yr,end_rule,note_id,obj_type,sys_id,geo_src,compiler,gecomplr,checker,ent_date,beg_chg_ty,end_chg_ty,geom
    name_py='null'
    if (abbrlist[0]!=''):
        name_py="'"+abbrlist[0]+"'"
    name_ch='null'
    if (abbrlist[1]!=''):
        name_ch="'"+abbrlist[1]+"'"
    name_ft='null'
    if (abbrlist[2]!=''):
        name_ft="'"+abbrlist[2]+"'"
    x_coor='null'
    if (abbrlist[3]!=''):
        x_coor=abbrlist[3]
    y_coor='null'
    if (abbrlist[4]!=''):
        y_coor=abbrlist[4]
    pres_loc='null'
    if (abbrlist[5]!=''):
        pres_loc="'"+abbrlist[5]+"'"
    type_py='null'
    if (abbrlist[6]!=''):
        type_py="'"+abbrlist[6]+"'"
    type_ch='null'
    if (abbrlist[7]!=''):
        type_ch="'"+abbrlist[7]+"'"
    lev_rank='null'
    if (abbrlist[8]!=''):
        lev_rank="'"+abbrlist[8]+"'"
    beg_yr='null'
    if (abbrlist[9]!=''):
        beg_yr=abbrlist[9]
    beg_rule='null'
    if (abbrlist[10]!=''):
        beg_rule="'"+abbrlist[10]+"'"
    end_yr='null'
    if (abbrlist[11]!=''):
        end_yr=abbrlist[11]
    end_rule='null'
    if (abbrlist[12]!=''):
        end_rule="'"+abbrlist[12]+"'"
    note_id='null'
    if (abbrlist[13]!=''):
        note_id=abbrlist[13]
    obj_type='null'
    if (abbrlist[14]!=''):
        obj_type="'"+abbrlist[14]+"'"
    sys_id='null'
    if (abbrlist[15]!=''):
        sys_id=abbrlist[15]
    geo_src='null'
    if (abbrlist[16]!=''):
        geo_src="'"+abbrlist[16]+"'"
    compiler='null'
    if (abbrlist[17]!=''):
        compiler="'"+abbrlist[17]+"'"
    gecomplr='null'
    if (abbrlist[18]!=''):
        gecomplr="'"+abbrlist[18]+"'"
    checker='null'
    if (abbrlist[19]!=''):
        checker="'"+abbrlist[19]+"'"
    ent_date='null'
    if (abbrlist[20]!=''):
        ent_date="'"+abbrlist[20]+"'"
    beg_chg_ty='null'
    if (abbrlist[21]!=''):
        beg_chg_ty="'"+abbrlist[21]+"'"
    end_chg_ty='null'
    if (abbrlist[22]!=''):
        end_chg_ty="'"+abbrlist[22]+"'"
    geom='null'
    if (abbrlist[23]!=''):
        geom="st_geomfromtext('"+abbrlist[23]+"',4326)"
    # ƴ��sql���
    sqltxt="INSERT INTO v6_time_pref_pts_utf_wgs84(" \
           "name_py,name_ch,name_ft,x_coor,y_coor,pres_loc,type_py,type_ch,lev_rank,beg_yr,beg_rule," \
           "end_yr,end_rule,note_id,obj_type,sys_id,geo_src,compiler,gecomplr,checker,ent_date," \
           "beg_chg_ty,end_chg_ty,geom) VALUES("+name_py+","+name_ch+","+name_ft+","+x_coor+","+y_coor+","\
           +pres_loc+","+type_py+","+type_ch+","+lev_rank+","+beg_yr+","+beg_rule+","+end_yr+","+end_rule+","\
           +note_id+","+obj_type+","+sys_id+","+geo_src+","+compiler+","+gecomplr+","+checker+","+ent_date+","\
           +beg_chg_ty+","+end_chg_ty+","+geom+")"
    print(sqltxt)
    # ִ��sql
    cur.execute(sqltxt)
# �ر�����
conn.commit()
conn.close()
print('�������')
