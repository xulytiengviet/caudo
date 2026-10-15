# CAUDO — Bitcoin Puzzle Intelligence Dashboard

Dashboard giám sát và truy vết nguồn gốc các thử thách Bitcoin, phục vụ nghiên cứu lịch sử giai đoạn 2001–2026 (Bitcoin từ 2009; chuỗi Bitcoin Puzzle Transaction từ 2015).

**Thiết kế:** Long Ngo. **Giấy phép:** MIT.

## Truy cập
- GitHub Pages (khi được bật): https://xulytiengviet.github.io/caudo/
- Dùng trực tiếp: mở `index.html` trong trình duyệt.

## Chức năng
- Dashboard responsive, lọc 160 ID, tìm kiếm, niên biểu, danh mục nguồn.
- Xuất CSV và JSON kèm snapshot và nguồn tham chiếu.
- Phân biệt số liệu tổng hợp của nguồn và chứng cứ từng địa chỉ.
- 160 ID là bộ khung dữ liệu nghiên cứu; hiện chỉ một số địa chỉ được điền sau đối chiếu trực tiếp trên LotteryPuzzle. Không suy đoán trạng thái những ID chưa nhập.
- Biểu đồ niên biểu là số **mốc trong hồ sơ**, không phải số puzzle đã giải theo năm.

## Phương pháp
Snapshot thống kê: [LotteryPuzzle 02/10/2026](https://lotterypzl.org/puzzles/?f=all) — 160 địa chỉ, 83 spent, 77 unspent. Đây **không phải dữ liệu blockchain live**. Danh mục nguồn mở rộng từ [Crypto Puzzle Atlas](https://github.com/itsnex1s/crypto-puzzle-list), BitcoinTalk, BTC Puzzle Info và kho lưu Internet Archive. Các số liệu, địa chỉ, trạng thái và ngày tháng phải được đối chiếu riêng bằng TXID/nguồn gốc trước khi xuất bản như một kết quả kiểm toán.

Không lưu seed, private key, WIF hay dữ liệu kiểm soát ví. Mã nguồn frontend không tự động dò khóa.

## Mở rộng
Đề xuất triển khai pipeline GitHub Actions (sau khi có đầu vào dữ liệu JSON/CSV đáng tin cậy), chạy theo lịch, chụp snapshot, kiểm tra TXID và xác nhận thay đổi trước khi cập nhật danh mục. Tránh gửi yêu cầu tần suất cao đến website ngoài và lưu ý CORS / rate limits.

© 2026 Long Ngo — MIT.
