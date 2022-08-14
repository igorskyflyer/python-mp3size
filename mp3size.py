def __bitrateInBits(rate: int):
    if rate >= 8:
        return rate // 8
    else:
        return 160 // 8


def __sizeInBits(size: int):
    return size * 8


def __getDuration(time: str):
    try:
        params = time.split(":")
        count = len(params)

        # assuming MM:ss format
        if count == 2:
            minutes = params[0]
            seconds = params[1]

            return int(minutes) * 60 + int(seconds)

        # assuming HH:MM:ss format
        elif count == 3:
            hours = params[0]
            minutes = params[1]
            seconds = params[2]

            return int(hours) * 3600 + int(minutes) * 60 + int(seconds)
        else:
            return -1
    except:
        return -1


def __padNumber(value: int):
    if value < 10:
        return "0" + str(value)
    else:
        return str(value)


def getFileSize(time: str, rate: int = 160):
    audioDuration = __getDuration(time)

    if audioDuration > -1:
        return audioDuration * __bitrateInBits(rate)
    else:
        return -1


def getAudioDuration(size: int, rate: int):
    if size == 0 or rate > size:
        return "-1"
    else:
        try:
            audioDuration = __sizeInBits(size) // rate

            if audioDuration > 0:
                audioDuration = round(audioDuration)

                hours = audioDuration // 3600
                minutes = (audioDuration - hours * 3600) // 60
                seconds = audioDuration % 60

                return (
                    __padNumber(hours)
                    + ":"
                    + __padNumber(minutes)
                    + ":"
                    + __padNumber(seconds)
                )
            else:
                return "00:00:00"
        except:
            return "-1"


def getAudioBitrate(time: str, size: int):
    audioDuration = __getDuration(time)

    if audioDuration > -1:
        try:
            return round(__sizeInBits(size) // audioDuration)
        except:
            return -1
    else:
        return -1
