> Execution note: this is the complete product brief, retained as the product source. Suggested stack, limits, sequencing and optional features require the relevant approval gate; implementation order and status are owned by [the phase index](../plan/README.md). Read [the specification index](README.md) for focused technical contracts and [decisions](../plan/decisions.md) for approved changes. This brief is not evidence of implemented functionality.

# DOKUMEN FINAL TERPADU — POTHOLE INSPECTION AI

**Sistem Pelaporan dan Inspeksi Lubang Jalan Berbantuan AI**
**Tujuan:** spesifikasi konsep proyek mata kuliah Artificial Intelligence dan brief visual.
**Status:** rancangan MVP; bukan aplikasi yang sudah dibangun, hasil eksperimen, atau bukti keamanan produksi.

## 1. Cara menggunakan dokumen ini

Dokumen ini berdiri sendiri dan menggantikan seluruh brief serta prompt sebelumnya sebagai acuan konsep. Tidak perlu membuka file lain untuk memahami proyek. Jika file lama atau `VISUALISASI ALUR.png` bertentangan dengan dokumen ini, ikuti dokumen ini. File lama tetap disimpan sebagai arsip, bukan sumber persyaratan tambahan.

Untuk AI image generator: baca ringkasan, alur operasional, serta bagian **PROMPT UNTUK AI IMAGE GENERATOR**. Bagian teknis menjaga konsistensi sistem; jangan memaksakan seluruh detail ke dalam satu gambar.

### Tingkat kepastian keputusan

- **Ditetapkan pengguna:** dua POV; masyarakat mengunggah video; admin memproses secara batch berkala; skala kecil; akurasi tidak harus sempurna.
- **Baseline desain hasil review:** batch dimulai manual, hasil diverifikasi admin, tidak ada inferensi saat upload, tidak ada counter lubang unik pada MVP.
- **Rekomendasi teknis:** stack dan batas upload di dokumen ini adalah baseline usulan untuk implementasi; belum diuji atau dikonfirmasi sebagai pilihan framework pengguna.
- **Belum diverifikasi:** kompatibilitas runtime dan performa bobot yang sudah diunduh, dataset/lisensi spesifik, hardware, waktu proses, biaya, deployment, rubrik dan deadline resmi mata kuliah.

### Ringkasan satu paragraf

Masyarakat mengirim video kondisi jalan beserta lokasi ruas dan tanggal melalui web. Sistem memvalidasi dan menyimpan laporan tanpa menjalankan AI. Admin login, meninjau, menolak atau memilih video, lalu memulai batch secara manual pada waktu yang ditentukan, misalnya seminggu sekali. Worker Python memproses video satu per satu menggunakan detector pothole dan menyimpan bukti beranotasi serta timestamp. Admin memeriksa hasil per video dan mencatat keputusan; AI tidak memastikan jumlah lubang unik, tingkat kerusakan, atau penyelesaian perbaikan. Penghematan komputasi adalah potensi dari seleksi dan pembatasan pemrosesan, bukan manfaat batching yang sudah terbukti.

## 2. Konsep inti

**Nama kerja:** Pothole Inspection AI — Sistem Pelaporan dan Inspeksi Lubang Jalan Berbantuan AI.

Prototipe web untuk proyek mata kuliah Artificial Intelligence, dengan dua sudut pandang:
- **Masyarakat:** mengirim laporan kondisi jalan beserta video melalui form web.
- **Admin/pemerintah:** meninjau dan memilih laporan, lalu memulai analisis AI atas sekumpulan video sebagai satu batch secara berkala.

Hasil deteksi digunakan sebagai bantuan pemeriksaan. Admin tetap menentukan apakah hasil relevan dan apa tindak lanjutnya. Aplikasi ini adalah prototipe pembelajaran, bukan sistem pemerintah yang sudah diterapkan.

## 3. Alur operasional yang dikunci

1. Masyarakat membuka halaman laporan.
2. Pelapor mengisi lokasi jalan dan tanggal pengambilan video, lalu mengunggah video. MVP tidak meminta nama atau kontak pribadi; pelapor menyetujui penggunaan video untuk analisis.
3. Sistem memvalidasi input dan menyimpan laporan serta video. Masyarakat menerima konfirmasi bahwa laporan **diterima**, bukan bahwa kerusakan sudah dikonfirmasi atau diperbaiki.
4. Laporan masuk ke daftar admin. Upload **tidak memicu AI**.
5. Admin meninjau laporan dan memilih video yang relevan dan layak; video yang tidak relevan, tidak layak, atau diduga duplikat dapat disisihkan atau ditolak dengan alasan. Duplikasi diputuskan oleh admin, bukan diasumsikan terdeteksi AI.
6. Pada waktu pemeriksaan berkala, misalnya seminggu sekali, admin menekan **Proses Batch**. Ini adalah keputusan manual; tidak ada penjadwalan otomatis yang dijanjikan. Untuk demo, tombol dapat ditekan kapan saja.
7. Sistem menganalisis video terpilih satu per satu dalam satu batch. Model computer vision mendeteksi dugaan pothole pada frame video. Kegagalan satu video dicatat per video dan tidak seharusnya menghentikan video lain.
8. Admin melihat hasil per video: frame bukti dengan bounding box dan timestamp. Jika tidak ada deteksi atau proses gagal, sistem menyatakan statusnya secara jelas.
9. Admin memberi keputusan per video: Ada dugaan terkonfirmasi, Tidak ada dugaan terkonfirmasi, atau Perlu pemeriksaan lanjutan, disertai catatan. Tindak lanjut dicatat manual bila fitur ini tersedia.

## 4. Peran dan batas MVP

### Masyarakat
- Form laporan: lokasi jalan, tanggal pengambilan video, dan file video.
- Konfirmasi penerimaan. Tidak ada akun masyarakat pada MVP.
- Tidak menjalankan model, mengakses dashboard admin, atau menentukan hasil validasi.

### Admin/pemerintah
- Login admin sederhana, melihat daftar laporan dan videonya.
- Memilih video untuk batch atau menyisihkan laporan dengan alasan.
- Memulai batch secara manual serta melihat status dan hasil tiap video.
- Memverifikasi hasil; mencatat tindak lanjut secara manual sebagai fitur tambahan jika waktu memungkinkan.
- Untuk demo, admin dapat memilih dan memproses batch segera; interval mingguan hanyalah contoh operasional, bukan timer yang berjalan otomatis.

### Di luar MVP
- Penjadwalan otomatis, pemrosesan real-time, aplikasi mobile terpisah, GPS otomatis tiap pothole, prediksi tingkat kerusakan, atau prioritas perbaikan otomatis.
- Portal publik untuk melacak status dan notifikasi pelapor tidak diwajibkan.
- Deteksi duplikat lintas video dan perhitungan jumlah pothole unik berada di luar MVP. Jangan menjumlahkan bounding box antar-frame sebagai jumlah lubang.
- Tidak ada klaim bahwa deteksi AI membuktikan jalan sudah diperbaiki.

## 5. AI dan batch: penjelasan yang benar

Video diproses melalui ekstraksi/sampling frame, lalu model object detection yang dilatih untuk pothole menghasilkan dugaan lokasi pothole pada frame. Hasil disimpan sebagai frame bukti, bounding box, timestamp, dan status pemrosesan. Sampel frame yang terlalu jarang dapat melewatkan pothole; pilihan interval perlu diuji pada video yang tersedia.

Pemrosesan seminggu sekali **tidak dengan sendirinya mengurangi total komputasi** dibanding menganalisis video yang sama satu per satu. Penghematan potensial berasal dari seleksi video, penghindaran video duplikat/tidak layak, batas durasi dan sampling frame, serta tidak perlu menjalankan layanan AI terus-menerus. Besarnya penghematan belum diukur.

Model dapat menghasilkan false positive atau melewatkan lubang. Tidak ada jaminan lokasi GPS tepat, kedalaman, tingkat keparahan, ataupun jumlah unik. Lokasi yang dimasukkan pelapor adalah lokasi ruas secara perkiraan, bukan GPS tiap lubang. Uji model dengan video yang relevan, termasuk jalan tanpa lubang, bayangan, pencahayaan buruk, dan kamera bergerak. Pisahkan pengujian berdasarkan perjalanan/video, bukan frame berdekatan dari video yang sama. Catat jumlah contoh dan temuan benar maupun salah; jangan mengklaim angka akurasi tanpa pengukuran yang jelas. Periksa lisensi model, bobot, dan dataset sebelum digunakan.

Pengaturan sampling, waktu batch, kapasitas penyimpanan, dan biaya belum ditentukan: uji dengan video serta perangkat yang tersedia. Proses batch juga tetap memerlukan waktu peninjauan manusia.

## 6. Arsitektur konseptual sederhana

**Masyarakat → form web → validasi → penyimpanan video + data laporan → inbox admin → seleksi → tombol Proses Batch → worker/proses AI → hasil per video → verifikasi admin.**

- File video dan bukti disimpan di storage; metadata, status, dan rujukan file disimpan di database. Pada prototipe, storage boleh berupa direktori lokal dan database lokal; tidak perlu cloud.
- Admin memulai batch melalui aplikasi; API menyimpan pekerjaan ke database dan worker Python terpisah mengambilnya. Inferensi tidak berjalan di request upload atau request tombol batch.
- Upload dan proses AI adalah dua tahap terpisah. Setiap laporan memiliki ID agar hasil terhubung ke video yang benar. Satu file gagal tidak menghentikan keseluruhan batch; status gagal dan opsi retry ditampilkan per video, tanpa menggandakan hasil yang telah berhasil.
- Video disimpan privat untuk admin; autentikasi dan pemeriksaan hak akses admin, validasi tipe/ukuran file, serta pembatasan upload dasar perlu ada. Tentukan masa simpan dan penghapusan data sebelum penggunaan nyata. Jangan memakai data pribadi atau video tanpa izin untuk demo.

## 7. Status sederhana

Gunakan tiga status terpisah agar laporan tidak disalahartikan sebagai hasil AI:
- **Seleksi laporan:** Diterima → Dipilih / Ditolak. Admin dapat mengubah pilihan sebelum batch dimulai.
- **Pemrosesan AI (label UI):** Belum diproses → Dalam antrean → Diproses → Selesai / Gagal / Terinterupsi. `Selesai` dapat berarti ada atau tidak ada deteksi; keduanya bukan keputusan admin.
- **Verifikasi hasil per video:** Belum ditinjau → Ada dugaan terkonfirmasi / Tidak ada dugaan terkonfirmasi / Perlu pemeriksaan lanjutan, disertai catatan untuk temuan campuran benar/salah. Video gagal diproses tidak dianggap mempunyai hasil AI sukses. Tidak adanya deteksi bukan bukti jalan bebas lubang; keputusan review bukan bukti jalan sudah diperbaiki.

## 8. Kriteria demo dan pengujian inti

1. Upload video valid dan metadata menghasilkan laporan tersimpan; AI tidak berjalan saat upload.
2. File tidak valid atau melewati batas yang ditetapkan ditolak dengan pesan yang jelas.
3. Admin memilih lebih dari satu video dan memulai satu batch secara manual.
4. Tiap video memiliki hasil/status sendiri: selesai dengan bukti, selesai tanpa deteksi, atau gagal. Satu kegagalan tidak menghentikan video lain.
5. Admin melihat bukti dan mengubah status verifikasi secara manual.
6. Hasil, keterbatasan, contoh salah deteksi, dan video yang tidak berhasil dianalisis ditunjukkan dengan jujur.

## 9. Keputusan stack dan deployment

Rekomendasi default untuk tim proyek kecil, belum merupakan pilihan framework yang dikonfirmasi pengguna:

| Bagian | Pilihan MVP | Alasan / batas |
|---|---|---|
| Web | FastAPI + Jinja2 + CSS + JavaScript sederhana | Satu proyek Python, same-origin; tidak perlu frontend build terpisah |
| API dan validasi | FastAPI, Pydantic, UploadFile | Validasi server wajib; upload dibaca bertahap dengan batas byte |
| Data | SQLite + SQLAlchemy + migrasi Alembic | Satu host, transaksi pendek, WAL dan busy timeout; bukan penyimpanan file besar |
| AI worker | Proses Python terpisah, polling tabel pekerjaan | Tidak mengunci request web dan antrean tetap tersimpan setelah restart |
| Video/AI | FFmpeg/ffprobe, OpenCV, detector pothole melalui Ultralytics | Harus menguji decoder dan bobot yang dipilih; pin dependency setelah pilot |
| Storage | Folder privat lokal di disk persisten | Database menyimpan ID/path relatif, bukan video sebagai BLOB |
| Auth admin | Session cookie server-side + hash password Argon2 | Satu role admin; tidak perlu signup publik, JWT atau OAuth |
| Demo | Satu komputer, satu server web dan satu worker | CPU dahulu; GPU opsional hanya setelah izin pengguna; hardware belum dibenchmark |

Tidak perlu Redis, Celery, Kubernetes, Docker, cloud storage, React, atau database server pada MVP ini. Ini pilihan pengurangan kompleksitas, bukan larangan pengembangan berikutnya. Jangan menaruh database WAL pada network filesystem atau menjalankan banyak host atas file yang sama.

Bila demo dipublikasikan: satu host persisten dengan HTTPS reverse proxy, autentikasi, batas request/upload, ruang disk terpantau, backup dan pembatasan akses. Jangan menaruh inferensi panjang atau file lokal permanen pada deployment serverless/ephemeral. Hosting publik dan kapasitasnya belum diputuskan; demo lokal adalah baseline, bukan janji portal internet siap produksi.

## 10. System design dan trigger

```text
Masyarakat -> form web -> validasi upload (bukan inferensi)
                         -> private storage + reports di DB
Admin login -> inbox -> tinjau -> pilih ID laporan
            -> POST batch -> transaksi membuat batch + batch_items
Worker Python -> ambil item antrean -> decode/sampling -> deteksi
              -> simpan evidence + hasil -> commit status tiap item
Dashboard -> polling status -> hasil per video -> review admin
```

Membuat batch hanya lewat tindakan admin yang terautentikasi. Tidak ada scheduler mingguan otomatis dan tidak ada AI saat upload. Worker menunggu pekerjaan; pemuatan model dan inferensi baru dilakukan saat ada batch yang disahkan. Cadence mingguan adalah prosedur operasional.

Batch berarti kelompok pekerjaan; MVP memproses video secara berurutan, bukan semua video secara paralel. Batasi satu batch aktif. Pemilihan admin menghasilkan snapshot ID video saat tombol dikonfirmasi; upload baru tidak ikut batch yang sedang berjalan. Tombol nonaktif di UI bukan proteksi: backend juga harus menolak klik ganda/batch bersamaan dalam transaksi.

## 11. Antrean, recovery, retry

- Batch: `Queued`, `Running`, `Completed`, `CompletedWithErrors`, `Failed`, `Interrupted`. Empty batch ditolak. Batch seluruhnya gagal = `Failed`; campuran berhasil/gagal = `CompletedWithErrors`.
- Item video: `Queued`, `Running`, `Succeeded`, `Failed`, `Interrupted`. Progress tampilkan jumlah item selesai dari total; jangan menampilkan persen inferensi detail yang tidak diukur.
- Klaim item memakai transaksi pendek dan kondisi status agar tidak diproses ganda. Jangan tahan transaksi SQLite selama inferensi.
- Hasil sukses disimpan lebih dulu melalui file sementara lalu rename atomik; status sukses hanya di-commit setelah artefak tersedia. Kegagalan penulisan tidak boleh menjadi sukses palsu.
- Jika worker restart/mati, pekerjaan `Running` yang ditinggalkan ditandai `Interrupted` setelah dipastikan tidak ada worker lama yang masih aktif. Admin melihat pesan pemulihan dan menekan retry; tidak ada klaim resume frame otomatis.
- Retry hanya item gagal/interrupted dan membuat attempt baru. Hasil sukses tidak diproses ulang oleh retry. Hindari overwrite bukti lama dan hasil duplikat lewat run/attempt ID serta pembatasan hasil per attempt.
- Timeout per video dan batas bukti disimpan sebagai konfigurasi; pilih nilainya lewat pilot. Jika satu decoder/inferensi macet, hentikan subprocess video tersebut, tandai gagal dan lanjutkan item berikutnya.
- Pembatalan batch, distributed workers, automatic retry kompleks dan reanalysis video sukses adalah non-goal MVP.

## 12. Model data minimal

Semua ID dibuat server. Waktu tersimpan UTC, tampilan WIB. Lokasi berupa teks ruas jalan yang diberikan pelapor, bukan koordinat pothole.

- `reports`: id UUID, road_location, observed_date, received_at, video_storage_key, original_filename (hanya metadata), size_bytes, duration_sec, selection_status, rejection_reason, created_at.
- `batches`: id, created_by_admin_id, created_at, status, started_at, finished_at.
- `batch_items`: id, batch_id, report_id, attempt_number, status, error_code, safe_error_message, started_at, finished_at, model_identifier, weights_hash, confidence_threshold, sampling_setting. Simpan konfigurasi aktual agar hasil dapat ditelusuri.
- `detections`: id, batch_item_id, timestamp_sec, bounding_box_xyxy, confidence, evidence_storage_key. Koordinat harus jelas dalam pixel frame asli beserta ukuran frame. Frame yang ditampilkan dengan resize harus mempertahankan penempatan box.
- `reviews`: id, report_id, batch_item_id, outcome, note, reviewed_by, reviewed_at. Review mengacu attempt hasil yang diperiksa.
- `admins` dan `sessions`: akun admin dan session server-side. `action_log`: siapa, kapan, tindakan, report/batch ID; jangan log password atau isi pribadi.

Relasi: satu report dapat mempunyai beberapa attempt; satu batch mempunyai banyak item; satu item mempunyai banyak deteksi. Pisahkan status seleksi laporan, status item AI, dan keputusan review. Jangan menyimpan tiga sumber status AI yang dapat berbeda tanpa aturan sinkronisasi; dashboard membaca attempt terbaru yang relevan.

## 13. Kontrak hasil dan review

- Minimum AI: annotated evidence frame, timestamp, confidence deteksi dan status per video. `Succeeded` dengan daftar deteksi kosong berbeda dari `Failed`.
- Confidence bukan akurasi sistem. Jumlah record deteksi bukan jumlah lubang unik. UI tidak menyediakan counter lubang unik pada MVP.
- Bounding box dibuat untuk dugaan objek; tidak perlu menghasilkan video beranotasi penuh. Batasi jumlah frame bukti agar hasil tidak memenuhi disk; tampilkan bahwa bukti adalah sampel, bukan seluruh inspeksi.
- Review per video: `Belum ditinjau`, `Ada dugaan terkonfirmasi`, `Tidak ada dugaan terkonfirmasi`, `Perlu pemeriksaan lanjutan` + catatan. Ini mencakup hasil campuran benar/salah serta video tanpa deteksi. Admin dapat menolak sebagian temuan lewat catatan; anotasi ulang kotak tidak wajib.
- `Tidak ada dugaan terkonfirmasi` hanya kesimpulan pemeriksaan video, bukan jaminan ruas bebas lubang. Video gagal tidak boleh direview seolah ada hasil AI sukses.
- Road maintenance bukan status AI/review. Jika fitur tindak lanjut ditambahkan, gunakan catatan manual terpisah; tidak menyatakan `Repaired` hanya karena tidak ada deteksi.

## 14. Upload dan keamanan dasar

Default usulan demo: satu MP4 per laporan, maksimum 100 MB dan 60 detik, codec video H.264, maksimum 1920×1080. Tim perlu menguji file ponsel yang tersedia dan mengubah batas bila perlu. Ekstensi MP4 sendiri tidak menjamin codec didukung. Jelaskan format yang diterima di form; tidak perlu auto-transcode HEVC pada MVP.

- Wajib: lokasi ruas, tanggal pengambilan, video, persetujuan pengiriman untuk analisis. Tolak tanggal masa depan berdasarkan tanggal WIB. Nama, nomor telepon dan email tidak dikumpulkan pada MVP.
- Validasi server: batas byte saat streaming, tipe file nyata dan probe decoder terbatas waktu, durasi/resolusi, video track valid. Jangan percaya MIME/ekstensi saja. File rusak/parsial tidak tampil sebagai laporan siap diproses.
- Tulis sementara, validasi, pindah ke storage final, buat laporan; bersihkan artefak parsial bila gagal. Rekonsiliasi file yatim bila crash terjadi antara storage dan transaksi DB.
- Nama file storage acak dibuat server; tidak pakai path/filename kiriman pengguna. Jangan menjalankan filename dengan shell interpolation. Jalankan decoder/worker tanpa hak admin OS.
- File asli dan bukti tidak di direktori static publik; endpoint streaming memeriksa session admin untuk setiap ID. UUID bukan otorisasi.
- Login dengan hash password, session expiry, logout yang membatalkan session; cookie HttpOnly, SameSite dan Secure pada HTTPS. Semua aksi mutasi admin dilindungi CSRF. Kredensial tidak masuk repo atau diagram.
- Batasi request/rate, upload bersamaan dan kapasitas disk; tolak upload baru dengan pesan jelas bila kuota habis. Angka kuota dipilih dari kapasitas host, bukan dikarang sebagai hasil uji.
- Retensi usulan demo 30 hari, bukan ketentuan hukum; pastikan ada proses penghapusan video, evidence dan referensi yang konsisten. Penghapusan data pengguna tetap memerlukan otorisasi operator dan kebijakan yang disepakati. Tidak ada penghapusan aktual dalam QC ini.
- Backup DB secara konsisten beserta file yang dirujuk; menyalin DB WAL aktif sembarangan tidak cukup. Uji restore terpisah sebelum mengklaim backup berhasil.

## 15. Screen dan acceptance criteria

1. **Form masyarakat:** label/batas file, progress upload, error validasi dan retry, konfirmasi dengan ID referensi. ID bukan portal tracking publik. Tidak ada klaim AI selesai pada konfirmasi.
2. **Login admin:** login berhasil/gagal, session habis, logout; akses langsung endpoint terlindungi tanpa session ditolak.
3. **Inbox:** lokasi/tanggal/status dan preview video privat; empty state, filter status, pilih beberapa video, alasan penolakan wajib. Mengubah pilihan tidak memulai AI.
4. **Batch:** konfirmasi jumlah video, indikator worker offline, queued/running, hasil tiap video, partial failure dan retry. Reload browser tidak menghentikan pekerjaan. Start tanpa video dan start ganda ditolak server.
5. **Detail hasil:** lokasi dan metadata, evidence/timestamp, tanpa deteksi, gagal dan review terpisah. Error file hilang ditampilkan sebagai error, bukan 'tidak ada pothole'.

Uji wajib sebelum demo: upload valid; file kosong/rusak/oversize/codec tidak didukung; akses admin/file tanpa session; upload tidak memicu inference; selection tidak memicu inference; batch dua video dengan satu gagal; retry tanpa duplikasi; restart worker; upload baru di tengah batch; kosong tanpa deteksi; campuran true/false positives; review tersimpan dan tetap ada setelah reload; disk penuh/hasil gagal disimpan; backup dan restore contoh laporan beserta evidence.

Untuk evaluasi AI: lakukan pilot pertama sebelum membangun seluruh UI. Periksa bobot pothole yang benar, lisensi dan kesesuaian kamera. Pisahkan video/perjalanan train-validation-test untuk menghindari kebocoran frame berdekatan. Laporkan ukuran sampel, false positive/miss dan waktu aktual pada hardware yang disebutkan. Tanpa pilot model nyata, kelayakan AI dan kecepatan belum terverifikasi.

## 16. QC verdict dan sisa keputusan

**Layak sebagai rancangan MVP lokal**, dengan syarat model dan decoding berhasil pada pilot. **Belum terbukti aman/siap produksi:** tidak ada kode, penetration test, benchmark, restore test atau deployment yang diverifikasi dalam review ini.

Sebelum implementasi: konfirmasi stack usulan, hardware/hosting, bobot dan lisensinya, kapasitas/limit upload, serta rubrik mata kuliah. Ini keputusan terbuka, bukan pekerjaan yang diam-diam sudah selesai. Tidak perlu menambahkan fuzzy logic atau algoritma lain hanya untuk memperbanyak label AI tanpa kebutuhan/rubrik.

## 17. Penjelasan konsistensi dan kontrak operasional

- Status seleksi laporan, eksekusi AI, review, dan tindak lanjut adalah domain berbeda. Label UI bahasa Indonesia memetakan status item teknis: `Queued` = Dalam antrean, `Running` = Diproses, `Succeeded` = Selesai, `Failed` = Gagal, `Interrupted` = Terinterupsi. Belum diproses berarti belum ada attempt. Status batch adalah agregat, bukan keputusan kebenaran deteksi.
- Pemilihan dan pembuatan batch hanya menerima laporan yang belum pernah sukses diproses dan tidak sedang terikat item aktif. Retry untuk kegagalan membuat attempt baru dalam batch retry tersendiri. Reanalysis laporan sukses berada di luar MVP. Status seleksi dikunci selama item aktif.
- Saat worker tidak tersedia, pekerjaan tetap `Queued`; dashboard tidak mengklaim inferensi sedang berjalan. Worker memiliki indikator heartbeat untuk status ketersediaan, tetapi heartbeat kedaluwarsa saja tidak mengizinkan worker lain merebut pekerjaan tanpa memastikan proses lama berhenti.
- Seluruh video tetap disimpan privat. Video decoder boleh berjalan saat validasi upload untuk memeriksa kelayakan teknis; itu bukan inferensi AI. Seleksi admin tetap dibutuhkan untuk kelayakan visual dan relevansi.
- Mempertahankan hasil sukses dan membatasi waktu per video adalah kebutuhan implementasi yang harus diuji, bukan kemampuan yang telah dibuktikan dokumen ini.

## 18. Urutan implementasi dan gerbang penerimaan

1. **Pilot AI terlebih dahulu:** gunakan video berizin, pastikan bobot benar-benar mengenali pothole dan menghasilkan bukti bertimestamp. Rekam dependency, lisensi, hardware dan hasil aktual. Jika pilot gagal, perbaiki model/input sebelum membangun semua UI.
2. **Vertical slice:** satu upload valid → storage privat dan metadata → login admin → satu batch → satu hasil → review tersimpan. Tidak ada inferensi pada upload.
3. **Ketahanan alur:** tambahkan beberapa video, mixed failure, queue persisten, restart, retry dan proteksi start ganda.
4. **Keamanan dan data:** validasi server, akses file, CSRF/session, kapasitas disk, pembersihan file parsial dan uji backup/restore.
5. **Evaluasi dan demo:** jalankan acceptance criteria, dokumentasikan false positive/miss dan keterbatasan, lalu susun presentasi. Tidak mengarang angka atau menggunakan hasil simulasi sebagai hasil model.

### Skenario demo tanpa angka hasil rekaan

- Unggah video jalan yang relevan dan tunjukkan bahwa statusnya belum diproses.
- Unggah video lain, lakukan peninjauan dan penolakan dengan alasan bila tidak layak.
- Pilih beberapa video, mulai batch, lalu tampilkan progress per item.
- Perlihatkan bukti nyata, video tanpa deteksi jika ada, serta kegagalan terkontrol. Kegagalan yang sengaja disimulasikan harus diberi label simulasi.
- Admin menyimpan review dan memuat ulang halaman untuk memperlihatkan persistensi.
- Jelaskan bahwa demo dapat dimulai kapan saja; seminggu sekali adalah contoh jadwal operasional manual.

## 19. PROMPT UNTUK AI IMAGE GENERATOR

Buat **satu diagram alur sistem yang informatif dan mudah dibaca**, bukan screenshot aplikasi dan bukan poster promosi. Gunakan layout horizontal lebar, latar terang, tipografi kontras tinggi, gaya ilustrasi vektor profesional yang bersih, ikon sederhana, panah alur jelas, dan teks bahasa Indonesia yang ringkas. Tampilkan dua area peran yang dibedakan secara visual: **MASYARAKAT** dan **ADMIN / PEMERINTAH**, serta area **PEMROSESAN AI**. Jangan gunakan logo instansi nyata atau klaim implementasi pemerintah nyata.

Tampilkan urutan ini dengan panah yang tepat:

**MASYARAKAT**
1. `Isi lokasi dan tanggal`
2. `Upload video kondisi jalan`
3. `Laporan diterima`

Panah dari upload menuju **PENYIMPANAN LAPORAN DAN VIDEO**. Konfirmasi diterima kembali ke masyarakat. Tambahkan label yang terlihat: `Upload tidak otomatis menjalankan AI`.

**ADMIN / PEMERINTAH**
4. `Tinjau laporan masuk`
5. `Pilih video yang layak`
Cabang dari peninjauan: `Tidak layak / duplikat` → `Ditolak dengan alasan`, tanpa masuk ke AI.
6. `Mulai proses batch` dengan keterangan `Manual, misalnya seminggu sekali`

**PEMROSESAN AI**
7. `Worker AI: analisis video terpilih` — gambarkan beberapa video masuk sebagai satu batch, diproses satu per satu oleh computer vision.
8. `Hasil per video` — tampilkan ilustrasi frame jalan dengan bounding box di sekitar dugaan lubang serta ikon timestamp; sertakan kemungkinan `Tidak ada deteksi` atau `Gagal` secara ringkas.

Kembali ke **ADMIN / PEMERINTAH**:
9. `Verifikasi hasil AI`
10. `Catat tindak lanjut manual (opsional)`

Tambahkan catatan kecil yang terbaca: `AI membantu pemeriksaan; keputusan tetap oleh admin.` Gunakan panah terpisah dari penyimpanan ke admin dan dari tombol admin ke AI. **Jangan menggambar panah langsung yang menunjukkan upload otomatis menjalankan AI.** Jangan menggambarkan hasil deteksi sebagai perbaikan jalan otomatis, peta GPS akurat, atau jumlah pothole pasti. Tidak perlu grafik persentase atau angka kinerja.

Jika generator kesulitan merender teks, utamakan struktur diagram dan sisakan label singkat agar dapat dikoreksi secara manual setelah generasi.

## 20. Referensi teknis primer

- FastAPI, background task dan caveat pekerjaan berat: https://fastapi.tiangolo.com/tutorial/background-tasks/
- SQLite WAL, batas konkurensi dan filesystem: https://www.sqlite.org/wal.html
- Ultralytics predict, input video dan konfigurasi inferensi: https://docs.ultralytics.com/modes/predict/

Referensi mendukung mekanisme teknis; tidak membuktikan akurasi pothole, keamanan aplikasi ini, atau performa perangkat pengguna.

## Keputusan baseline pretrained
Detector awal menggunakan kandidat PeterHdd yang dipin di [manifest](../models/pothole-baseline.json), bukan training dari nol. Weights sudah diunduh, tetapi belum dijalankan atau dinyatakan cocok. [Kontrak AI](ai-and-dataset.md) mengatur evaluasi independen, lisensi dan fallback. Web, upload, worker dan human review tetap dikembangkan sesuai PRD; source project upstream hanya referensi, bukan aplikasi yang sudah diadopsi.
