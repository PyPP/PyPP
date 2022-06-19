from datetime import datetime
from plyer import notification
class Time:
    now = datetime.now()
    FullTime = now.strftime("%H:%M:%S")
    ShortTime = now.strftime("%H:%M")
    Short12Hr = now.strftime('%I:%M')
    Full12Hr = now.strftime('%I:%M:%S')
    Year = now.strftime('%Y')
    Month = now.strftime('%m')
    Day = now.strftime('%d')
    Date = Day + '-' + Month + '-' + Year

def SendNotifaction(Title, Message):
    notification.notify(
    title = Title,
    message = Message,
    timeout = 10,
    )
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def heythere():
	print("Hey There")