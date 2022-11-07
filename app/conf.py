ROLE_CHOICE = (('1', '負責主要照顧責任'), ('2', '協助家人顧顧與蒐集資訊'), ('3', '從事照顧相關工作的人'), ('4', '對照護議題感興趣'))
# ROLE_CHOICE = (('負責主要照顧責任','負責主要照顧責任'), ('協助家人顧顧與蒐集資訊','協助家人顧顧與蒐集資訊')
#                , ('從事照顧相關工作的人','從事照顧相關工作的人'), ('對照護議題感興趣','對照護議題感興趣'))


CARE_TIME_CHOICE = (('1','即將開始照顧'),('2','開始半年內'),('3','半年~1年'),('4','1年~3年'),('5','3年~5年'),('6','5年以上'))
SURVEY_CHOICE =(('5','非常同意'),('4','同意'),('3','沒有意見'),('2','不同意'),('1','非常不同意'))
RESIDENCE_CHOICE = (('0','新北市'),('1','台北市'),('2','桃園市'),('3','台中市'),('4','台南市'),
                    ('5','高雄市'),('6','宜蘭市'),('7','新竹縣'),('8','苗栗縣'),('9','彰化縣'),
                    ('10','南投縣'),('11','雲林縣'),('12','嘉義縣'),('13','嘉義市'),
                    ('14','屏東縣'),('15','台東縣'),('16','花蓮縣'),('17','澎湖縣'),('18','基隆市')
                    ,('19','新竹市'),('20','金門縣'),('21','連江縣'))

DISEASE_CHOICE = ((10,'健康無疾病'),(1,'中風'),(2,'癌症'),(3,'失智症'),(4,'糖尿病'),(5,'高血壓'),(6,'腎臟病')
                  ,(7,'帕金森氏症'),(8,'壓傷'),(9,'其他'))


MOBILITY_CHOICE = ((0,'行動自如'),(1,'不平坦地面行走吃力'),(2,'需攙扶或拿拐杖行走'),(3,'無法行走，可維持坐姿'),(4,'無法維持坐姿'))
DIFFICULT_CARE_CHOICE = ((0,'盥洗困難'),(1,'淋浴困難'),(2,'排尿排便困難'),(3,'如廁困難'),(4,'更衣困難')
                  ,(5,'進食困難'),(6,'移位困難'),(7,'步行困難'),(8,'上下樓困難'))
LIFE_CHOICE = ((0,'維持家務'),(1,'洗衣服'),(2,'烹調食物'),(3,'自己負責服藥'),(4,'上街購物')
                  ,(5,'外出活動'),(6,'使用電話'),(7,'處理財務'))
COHABITANT_CHOICE=((0,'獨居'),(1,'看護'),(2,'配偶'),(3,'您本人'),(4,'其他家人')
                  ,(5,'入住照護機構'))
RESOURCE_CHOICE=((0,'我不清楚'),(1,'長照2.0服務'),(2,'本國籍看護'),(3,'日間照護中心'),(4,'24hr機構照顧')
                  ,(5,'其他'))

EXCEPTION_CHOICE=((0,'自己照顧'),(1,'家人共同照顧'),(2,'長照2.0服務'),(3,'本國籍看護'),(4,'外籍看護')
                  ,(5,'24hr機構照顧'),(5,'自費照顧服務'))
BUDGET_CHOICE=((0,'1.5萬以下'),(1,'1.5萬~3萬'),(2,'3萬~4萬'),(3,'4萬~5萬'),(4,'5~7萬')
                  ,(5,'7~12萬'),(6,'12萬以上'))