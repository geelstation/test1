from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

adhkar_by_time = {
    "morning": [
        "أصبحنا وأصبح الملك لله والحمد لله",
        "سبحان الله وبحمده سبحان الله العظيم",
        "لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير",
        "اللهم ما أصبح بي من نعمة أو بأحد من خلقك فمنك وحدك لا شريك لك، فلك الحمد ولك الشكر"
    ],
    "noon": [
        "اللهم اجعلنا من الذين يستمعون القول فيتبعون أحسنه",
        "اللهم اغفر لنا وارحمنا وتب علينا إنك أنت التواب الرحيم",
        "اللهم اجعلنا من الذين لا خوف عليهم ولا هم يحزنون"
    ],
    "afternoon": [
        "سبحان الله وبحمده عدد خلقه ورضا نفسه وزنة عرشه ومداد كلماته",
        "اللهم إني أسألك علماً نافعاً ورزقاً طيباً وعملاً متقبلاً",
        "اللهم إني أعوذ بك من علم لا ينفع ومن قلب لا يخشع ومن نفس لا تشبع ومن دعوة لا يستجاب لها"
    ],
    "evening": [
        "اللهم أنت ربي لا إله إلا أنت، خلقتني وأنا عبدك وأنا على عهدك ووعدك ما استطعت",
        "اللهم اجعلنا من التوابين واجعلنا من المتطهرين",
        "اللهم صل وسلم على نبينا محمد وعلى آله وصحبه أجمعين"
    ],
    "night": [
        "اللهم إني أسألك العفو والعافية في الدنيا والآخرة",
        "يا حي يا قيوم برحمتك أستغيث، أصلح لي شأني كله ولا تكلني إلى نفسي طرفة عين",
        "اللهم إني أعوذ بك من الهم والحزن، وأعوذ بك من العجز والكسل، وأعوذ بك من الجبن والبخل، وأعوذ بك من غلبة الدين وقهر الرجال"
    ]
}

template = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>أذكار وأدعية اليوم</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #e0e0e0;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .adhkar-list {
            max-width: 600px;
            width: 100%;
            margin-top: 20px;
        }
        .adhkar-item {
            width: 100%;
            margin-bottom: 15px;
            padding: 15px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1), 0 0 10px rgba(0, 150, 136, 0.4);
            font-size: 18px;
            line-height: 1.6;
            text-align: center;
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }
        .adhkar-item:hover {
            transform: translateY(-5px);
            background-color: #f0f8ff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2), 0 0 15px rgba(0, 150, 136, 0.6);
        }
        h1 {
            color: #00796b;
            font-size: 28px;
            margin-bottom: 20px;
            text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.1);
        }
        .time {
            font-size: 20px;
            color: #555;
            margin-bottom: 15px;
            direction: ltr;
            text-align: center;
        }
        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }
            .adhkar-item {
                font-size: 16px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>أذكار وأدعية اليوم</h1>
        <p class="time">الوقت الحالي: {{ current_time }}</p>
        <div class="adhkar-list">
            {% if adhkar_list %}
                {% for adhkar in adhkar_list %}
                    <div class="adhkar-item">
                        <p>{{ adhkar }}</p>
                    </div>
                {% endfor %}
            {% else %}
                <p>لا توجد أذكار محددة في هذا الوقت. الرجاء السبحة.</p>
            {% endif %}
        </div>
    </div>
</body>
</html>
"""

def get_current_adhkar():
    now = datetime.now()
    if 5 <= now.hour < 12:
        return adhkar_by_time['morning']
    elif 12 <= now.hour < 15:
        return adhkar_by_time['noon']
    elif 15 <= now.hour < 18:
        return adhkar_by_time['afternoon']
    elif 18 <= now.hour < 20:
        return adhkar_by_time['evening']
    else:
        return adhkar_by_time['night']

@app.route('/')
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    adhkar_list = get_current_adhkar()
    return render_template_string(template, adhkar_list=adhkar_list, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
