def calculate_pps_score(data):
    try:
        total = sum(int(v) for v in data.values())
        percentage = int((total / (len(data) * 10)) * 100)
        return percentage
    except:
        return 0

def get_guideline(score):
    if score >= 70:
        return "ผู้ป่วยช่วยเหลือตนเองได้ดี ยังสามารถดูแลแบบประคับประคองที่บ้านได้"
    elif score >= 40:
        return "เริ่มต้องการการดูแลเพิ่มขึ้น อาจพิจารณาการดูแลร่วมกับทีม Palliative Care"
    else:
        return "ควรได้รับการดูแลอย่างใกล้ชิดโดยทีมดูแลแบบประคับประคองเต็มรูปแบบ"
