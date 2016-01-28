#
# SI Akademik manifest file
#
{
    'name': 'Sistem Informasi Akademik Perguruan Tinggi',
    'depends': ['base','hr','account','account_voucher', 'sale', 'purchase'],
    'author'  :'vitraining.com',
    'version': '0.3',
    "website" : "http://www.vitraining.com",
    'category': 'Tools',
    'description': """
Sistem Informasi Akademik Perguruan Tinggi yang sudah di sesuaikan dengan standar perguruan tinggi yang ada di Indonesia (Odoo v8)
""",
    'installable':True,
    'data': ['security/groups.xml',
            'security/ir.model.access.csv',
            'jadwal.xml',
            'akademik.xml',
    		'partner.xml',
            'wisuda.xml',
    		'spmb.xml',	
    		'operasional.xml',
    		'kelas.xml',
            'absensi.xml',           
            'kurikulum.xml',
            'cuti_kuliah.xml',
            'invoice.xml',
            'pembayaran.xml',
            'product.xml',
            'partner_calon_mhs.xml',
            'konversi.xml',
            'jadwal_usm.xml',
            'jenis_pendaftaran.xml',
            'reports/report.xml',
            'data/data_view.xml',
            'company.xml',
            'imports.xml',
            'imports_lsm.xml',
            'imports_mhs.xml',
            'imports_mk.xml',
            'imports_nlm.xml',
            'beasiswa_prodi.xml',
            'users.xml'
       ],
}
