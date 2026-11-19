# -*- coding: utf-8 -*-
{
    'name': 'Khoáng Sản Hoàng Phúc - Demo Data (Kho, Mua Hàng, Bán Hàng)',
    'version': '19.0.1.0.0',
    'summary': 'Dữ liệu mẫu chuẩn Odoo phục vụ hỏi đáp với AI về chủ đề khoáng sản Hoàng Phúc',
    'description': """
        Khoáng Sản Hoàng Phúc - Bộ dữ liệu mẫu chuẩn Odoo (Không thêm trường tùy biến):
        - Quản lý Nhà cung cấp (Mỏ khai thác, bao bì, hóa chất tuyển quặng, tàu vận tải)
        - Quản lý Khách hàng (Nhà máy kính Viglacera, thép Hòa Phát, sơn Nippon, PV Drilling, đối tác xuất khẩu POSCO Hàn Quốc...)
        - Danh mục và Sản phẩm khoáng sản (Cát thạch anh, Đá vôi CaCO3, Quặng Dolomite, Titan Ilmenite, Barite khoan...)
        - Quản lý Kho bãi & Tồn kho thực tế (Kho Cảng Đình Vũ Hải Phòng, Kho Nhà máy Nghi Sơn, Kho Mỏ Lào Cai)
        - Đơn Mua hàng (Purchase Orders) quặng thô, vật tư phụ trợ
        - Đơn Bán hàng (Sales Orders) giao nội địa & xuất khẩu
    """,
    'category': 'Sales/Inventory/Purchase',
    'author': 'Hoang Phuc Minerals',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'uom',
        'product',
        'stock',
        'purchase',
        'sale_management',
    ],
    'data': [
        'data/res_partner_data.xml',
        'data/product_category_data.xml',
        'data/product_data.xml',
        'data/stock_location_data.xml',
        'data/stock_quant_data.xml',
        'data/purchase_order_data.xml',
        'data/sale_order_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
