Ledger Entry API - README
Overview
Bu proje, bir LedgerEntry modelini kullanarak, ledger (defter) girişlerini işleyen bir API uygulamasıdır. Bu uygulama, bir dizi operasyon türünü içeren LedgerEntry nesnelerini oluşturmak, doğrulamak ve yönetmek için kullanılan temel sınıfları içerir.
Proje, FastAPI ile geliştirilmiş olup, veritabanı işlemleri için SQLAlchemy kullanmaktadır. Ayrıca, bir uygulama için özel App1LedgerOperation gibi işlemleri desteklerken, tüm uygulamalarda ortak olan işlemleri BaseLedgerOperation enum sınıfı ile yönetir.
Proje Yapısı
1. LedgerEntry Model
•	LedgerEntry modeli, veritabanında bir ledger girişini temsil eder.
•	Bu modelde id, operation, amount, nonce, owner_id, ve created_on gibi alanlar bulunmaktadır.
•	operation alanı, işlem türünü belirtmek için bir Enum kullanır ve her işlem bir değere sahiptir.
2. BaseLedgerOperation Enum
•	Bu Enum sınıfı, tüm uygulamalarda ortak olan işlemleri tanımlar.
•	validate_operations metoduyla uygulama işlemleri ile karşılaştırma yapılarak, gerekli işlemler doğrulanabilir.

3. App-Specific Operations
•	Özel uygulama işlemleri (örneğin App1LedgerOperation), BaseLedgerOperation ile doğrulanabilir.
•	Özel işlemler, LedgerOperationRegistry sınıfı aracılığıyla kaydedilir.
class App1LedgerOperation(Enum):
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"

4. LedgerOperationRegistry
•	Bu sınıf, işlemleri operasyon türlerine göre kaydetmek için kullanılır.
•	register_operations metodu ile işlem türleri kaydedilir ve get_all_operations ile tüm kayıtlı işlemler alınabilir.
5. Main Application
•	FastAPI uygulaması, ledger işlemleri ve API yönlendirmeleri için yapılandırılmıştır.
•	Veritabanı bağlantısı sağlanır ve ledger girişlerine dair işlemler yapılır.
•	
6. API Kullanımı
•	GET /ledger_entries: Tüm ledger girişlerini alır.
•	POST /ledger_entries: Yeni bir ledger girişini ekler.
•	GET /ledger_entries/{owner_id}: Belirli bir kullanıcının ledger girişlerini alır.
7.Yeni İşlem Ekleme
•	LedgerEntryCreate modeli kullanılarak yeni bir işlem(operation) oluşturulur.
•	İşlem, LedgerEntry tablosuna kaydedilir.


Uygulamaya Özel İşlemler (App1LedgerOperation)
 İşlem Kayıt Defteri (LedgerOperationRegistry)
İşlem Birleştirme (get_combined_operations)
Gibi fonksiyonlar da mevcuttur.

Örnek çıktı
Kayıtlı işlemler: ['DAILY_REWARD', 'SIGNUP_CREDIT', 'CREDIT_SPEND', 'CREDIT_ADD', 'CONTENT_CREATION', 'CONTENT_ACCESS']
Serkan Koçoğlu
