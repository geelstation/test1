from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

# Dictionary of adhkar and duas for different times and occasions
adhkar_data = {
    'fajr': [
        "سبحان الله وبحمده، سبحان الله العظيم",
        "اللهم صل على محمد وعلى آل محمد كما صليت على إبراهيم وعلى آل إبراهيم، إنك حميد مجيد"
    ],
    'zuhr': [
        "الله أكبر",
        "اللهم اجعلني من المقيمين الصلاة ومن ذرية قيم الصلاة"
    ],
    'asr': [
        "سبحان الله وبحمده",
        "اللهم إني أعوذ بك من العجز والكسل والجبن والبخل والهرم، وأعوذ بك من عذاب القبر"
    ],
    'maghrib': [
        "سبحان الله وبحمده، سبحان الله العظيم",
        "اللهم اجعل لي في قلبي نوراً، وفي لساني نوراً، واجعل لي في سمعي نوراً، واجعل لي من خلفي نوراً، ومن أمامي نوراً، واجعل لي من فوقي نوراً، ومن تحتي نوراً، اللهم أعطني نوراً"
    ],
    'isha': [
        "الله أكبر",
        "اللهم اغفر لي ولوالدي ولمن دخل بيتي مؤمناً وللمؤمنين والمؤمنات ولا تزد الظالمين إلا تباراً"
    ],
    'before_sleep': [
        "اللهم بسمك أموت وأحيا",
        "اللهم أعوذ بك من الهم والحزن، وأعوذ بك من العجز والكسل، وأعوذ بك من الجبن والبخل، وأعوذ بك من غلبة الدين وقهر الرجال",
        "اللهم إني أمسيت أشهدك وأشهد حملة عرشك وملائكتك وجميع خلقك أنك أنت الله لا إله إلا أنت، وأن محمداً عبدك ورسولك، أعوذ بك من شر نفسي ومن شر الشيطان وشركه وأن أقترف على نفسي سوءاً أو أجره إلى مسلم",
        "اللهم إني أمسيت أعوذ بك من الكفر والفقر، وأعوذ بك من عذاب القبر، لا إله إلا أنت"
    ],
    'morning': [
        "اللهم إني أسألك علماً نافعاً ورزقاً طيباً وعملاً متقبلاً",
        "اللهم أجعل لي من أمري فرجاً، ومن بين يدي فرجاً، ومن خلفي فرجاً، ومن فوقي فرجاً، ومن تحتي فرجاً، ومن عن يميني فرجاً، ومن عن شمالي فرجاً، ومن قدامي فرجاً، وأعطني ما أسألك",
        "اللهم إني أسألك العافية في الدنيا والآخرة"
    ],
    'evening': [
        "اللهم بك أمسينا، وبك أصبحنا، وبك نحيا، وبك نموت، وإليك المصير",
        "اللهم لك الحمد كله، ولك الحمد حتى ترضى، ولك الحمد إذا رضيت، ولك الحمد بعد الرضا",
        "اللهم إني أعوذ بك من الفقر، والقلة، وأعوذ بك من أن أظلم أو أُظلم، وأعوذ بك من الأدران وأعوذ بك من الشقاء"
    ],
    'special_occasion': [
        "ربنا آتنا في الدنيا حسنة وفي الآخرة حسنة وقنا عذاب النار",
        "اللهم اجعل القرآن ربيع قلوبنا، ونور صدورنا، وجلاء أحزاننا وذهاب همومنا",
        "اللهم إني أسألك علماً نافعاً، ورزقاً طيباً، وعملاً متقبلاً، وتوبةً عن كل ذنبٍ، وشفاءً من كل داء"
    ],
    'after_prayer': [
        "اللهم أنت السلام ومنك السلام، تباركت يا ذا الجلال والإكرام"
    ],
    'travel': [
        "اللهم إنا نعوذ بك من وعثاء السفر، وكآبة المنظر، وسوء المنقلب في المال والأهل"
    ],
    'sick': [
        "اللهم رب الناس، أذهب البأس، واشف أنت الشافي، لا شفاء إلا شفاؤك، شفاءً لا يغادر سقماً"
    ],
    'forgiveness': [
        "اللهم إني أعوذ بك من علمٍ لا ينفع، ومن قلبٍ لا يخشع، ومن نفسٍ لا تشبع، ومن دعاءٍ لا يُسمع"
    ],
    'tasbeeh': [
        "سبحان الله",
        "الحمد لله",
        "لا إله إلا الله",
        "الله أكبر"
    ]
}

def get_current_time():
    tz = pytz.timezone('Asia/Riyadh')  # Replace with user's timezone
    now = datetime.now(tz)
    current_time = now.strftime('%H:%M')
    return current_time

def get_current_prayer():
    # This function can be modified to fetch actual prayer times from an API or database
    current_time = get_current_time()

    if current_time >= '04:00' and current_time < '06:00':
        return 'fajr'
    elif current_time >= '12:00' and current_time < '14:00':
        return 'zuhr'
    elif current_time >= '15:00' and current_time < '17:00':
        return 'asr'
    elif current_time >= '18:00' and current_time < '20:00':
        return 'maghrib'
    elif current_time >= '20:00' and current_time < '22:00':
        return 'isha'
    else:
        return 'special_occasion'

@app.route('/')
def index():
    current_prayer = get_current_prayer()
    adhkar_list = adhkar_data.get(current_prayer, adhkar_data['tasbeeh'])  # Default to tasbeeh if no specific adhkar found

    return render_template('index.html', adhkar_list=adhkar_list, current_time=get_current_time())

if __name__ == '__main__':
    app.run(debug=True)
