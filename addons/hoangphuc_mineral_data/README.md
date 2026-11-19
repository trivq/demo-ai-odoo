# Khoáng Sản Hoàng Phúc — Odoo Demo Data (Kho, Mua Hàng, Bán Hàng)

Module dữ liệu mẫu **chuẩn 100% Odoo** (không khai báo model hay trường Python tùy biến nào), dùng trực tiếp trên **Odoo.sh** hoặc máy chủ Odoo cục bộ để demo tính năng **Hỏi đáp AI (Odoo AI / LLM)**.

---

## 1. Cấu trúc dữ liệu

| Lĩnh vực | File XML | Nội dung dữ liệu |
| :--- | :--- | :--- |
| **Đối tác** | `data/res_partner_data.xml` | • 6 Nhà cung cấp: Mỏ Hoàng Liên (Lào Cai), Mỏ đá Tam Điệp, Mỏ Titan Kỳ Anh, Hóa chất Đức Giang, Bao bì Jumbo Việt Hưng, Vận tải Thủy Duyên Hải.<br>• 7 Khách hàng: Kính nổi Viglacera, Thép Hòa Phát Dung Quất, Sơn Nippon Paint, PV Drilling, POSCO Daewoo (Hàn Quốc), Tokyo Ceramics (Nhật Bản), Gạch men Đồng Tâm. |
| **Danh mục** | `data/product_category_data.xml` | Cát & Bột Thạch Anh, Đá Vôi Canxit & Dolomite, Quặng Sa Khoáng Titan & Zircon, Khoáng Sản Công Nghiệp (Barite), Vật Tư Phụ Trợ & Bao Bì. |
| **Sản phẩm** | `data/product_data.xml` | 9 sản phẩm chính: Quặng thạch anh thô, Cát thạch anh lọc kính (SiO2 > 99.5%), Bột thạch anh 325 mesh, Đá vôi canxit thô, Bột đá CaCO3 siêu mịn tráng phủ axit béo, Quặng Dolomite luyện thép, Tinh quặng Titan Ilmenite 52% TiO2, Bột Barite khoan dầu khí 4.2 SG, Bao Jumbo 1 tấn. |
| **Kho bãi** | `data/stock_location_data.xml` | 3 địa điểm kho nội bộ: Kho Cảng Đình Vũ (Hải Phòng - Xuất khẩu), Kho Nhà máy Nghi Sơn (Thanh Hóa), Kho Bãi Mỏ Lào Cai. |
| **Tồn kho** | `data/stock_quant_data.xml` | Số dư tồn kho thực tế: 2.500 tấn cát thạch anh làm kính, 600 tấn bột thạch anh 325 mesh, 4.000 tấn thạch anh thô, 8.500 tấn đá canxit thô, 1.800 tấn bột đá siêu mịn, 3.200 tấn dolomite, 1.450 tấn tinh quặng titan, 950 tấn bột barite, 6.000 bao Jumbo. |
| **Mua hàng** | `data/purchase_order_data.xml` | 5 đơn mua hàng (PO-HP2026-001 đến 005): Mua 6.000 tấn thạch anh thô, 15.000 tấn đá canxit thô, 1.500 tấn titan thô, 8.000 vỏ bao Jumbo, báo giá axit béo tráng phủ. |
| **Bán hàng** | `data/sale_order_data.xml` | 7 đơn bán hàng (SO-HP2026-001 đến 007): Bán Viglacera (2,55 tỷ), Hòa Phát (5,44 tỷ), Nippon Paint (2,16 tỷ), POSCO Hàn Quốc (4,6 tỷ), PV Drilling (2,56 tỷ), Báo giá Tokyo Ceramics & Đồng Tâm. |

---

## 2. Hướng dẫn chạy trên Odoo.sh

1. **Đẩy mã nguồn lên Git:**
   ```bash
   git add addons/hoangphuc_mineral_data
   git commit -m "feat: thêm dữ liệu mẫu Khoáng Sản Hoàng Phúc"
   git push origin main
   ```
2. **Kích hoạt trên Odoo.sh:**
   - Odoo.sh sẽ tự động build nhánh.
   - Đăng nhập vào Odoo > bật chế độ **Developer Mode**.
   - Vào menu **Apps (Ứng dụng)** > Chọn **Update Apps List (Cập nhật danh sách ứng dụng)**.
   - Tìm kiếm từ khóa: `Khoáng Sản Hoàng Phúc` hoặc `hoangphuc_mineral_data`.
   - Bấm **Install (Cài đặt)**.

*(Toàn bộ dữ liệu Đối tác, Sản phẩm, Tồn kho, Đơn mua, Đơn bán sẽ được nạp tức thì vào database Odoo chuẩn).*

---

## 3. Bộ câu hỏi gợi ý để Demo Hỏi Đáp với AI

### A. Nhóm câu hỏi về Kho & Tồn kho
1. *"Tổng tồn kho Cát thạch anh lọc kính của Hoàng Phúc hiện còn bao nhiêu tấn?"*
   👉 **Đáp án AI trả về:** 2.500 tấn (tại Kho Cảng Đình Vũ Hải Phòng).
2. *"Tại Kho Nhà máy Nghi Sơn hiện đang có những mặt hàng nào và số lượng bao nhiêu?"*
   👉 **Đáp án AI trả về:** 8.500 tấn Đá canxit thô, 1.800 tấn Bột đá CaCO3 siêu mịn tráng phủ, 3.200 tấn Quặng Dolomite luyện thép và 6.000 vỏ bao Jumbo 1 tấn.
3. *"Bột Barite khoan dầu khí còn tồn kho không và lưu trữ ở kho nào?"*
   👉 **Đáp án AI trả về:** Còn 950 tấn tại Kho Cảng Đình Vũ (Hải Phòng).

### B. Nhóm câu hỏi về Bán hàng
1. *"Khách hàng nào có giá trị đơn hàng lớn nhất trong các đơn bán hàng gần đây?"*
   👉 **Đáp án AI trả về:** Công ty Cổ phần Thép Hòa Phát Dung Quất với đơn hàng SO-HP2026-002 giá trị 5.440.000.000 VNĐ (mua 8.000 tấn Quặng Dolomite).
2. *"Công ty Hoàng Phúc đã ký hợp đồng bán hàng xuất khẩu nào ra nước ngoài chưa?"*
   👉 **Đáp án AI trả về:** Có đơn SO-HP2026-004 xuất khẩu 1.000 tấn Tinh quặng Titan Ilmenite 52% TiO2 cho đối tác POSCO International Corporation (Hàn Quốc) trị giá 4,6 tỷ VNĐ (và báo giá SO-HP2026-006 gửi Tokyo Ceramics Nhật Bản).
3. *"Tổng công ty Viglacera đang mua sản phẩm gì và giá trị bao nhiêu?"*
   👉 **Đáp án AI trả về:** Mua 3.000 tấn Cát Thạch Anh Tinh Chế Làm Kính với đơn giá 850.000 đ/tấn, tổng giá trị hợp đồng là 2.550.000.000 VNĐ theo đơn SO-HP2026-001.

### C. Nhóm câu hỏi về Mua hàng & Cung ứng
1. *"Hoàng Phúc mua quặng thạch anh thô từ nhà cung cấp nào và đơn giá bao nhiêu?"*
   👉 **Đáp án AI trả về:** Mua từ Công ty TNHH Khai thác Mỏ Hoàng Liên - Lào Cai (đơn PO-HP2026-001), số lượng 6.000 tấn với đơn giá 350.000 đ/tấn.
2. *"Các đơn mua hàng đã hoàn tất nhập kho là đơn nào?"*
   👉 **Đáp án AI trả về:** Đơn PO-HP2026-003 mua 1.500 tấn quặng titan thô từ Mỏ Kỳ Anh - Hà Tĩnh (trạng thái Done).

### D. Nhóm câu hỏi tổng hợp chuỗi cung ứng
1. *"Tồn kho Cát thạch anh lọc kính hiện tại (2.500 tấn) có đáp ứng đủ đơn hàng SO-HP2026-001 của Viglacera (3.000 tấn) không?"*
   👉 **Đáp án AI trả về:** Hiện tồn kho đang có 2.500 tấn tại Kho Hải Phòng, còn thiếu 500 tấn để hoàn tất toàn bộ hợp đồng 3.000 tấn (tuy nhiên công ty có 4.000 tấn quặng thô tại mỏ Lào Cai và đang mua thêm 6.000 tấn theo đơn PO-HP2026-001 để tiếp tục chế biến).
