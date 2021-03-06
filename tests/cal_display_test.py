import datetime

from khal.calendar_display import vertical_month, getweeknumber, str_week


today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)


def test_getweeknumber():
    assert getweeknumber(datetime.date(2011, 12, 12)) == 50
    assert getweeknumber(datetime.date(2011, 12, 31)) == 52
    assert getweeknumber(datetime.date(2012, 1, 1)) == 52
    assert getweeknumber(datetime.date(2012, 1, 2)) == 1


def test_str_week():
    aday = datetime.date(2012, 6, 1)
    bday = datetime.date(2012, 6, 8)
    week = [datetime.date(2012, 6, 6),
            datetime.date(2012, 6, 7),
            datetime.date(2012, 6, 8),
            datetime.date(2012, 6, 9),
            datetime.date(2012, 6, 10),
            datetime.date(2012, 6, 11),
            datetime.date(2012, 6, 12),
            datetime.date(2012, 6, 13)]
    assert str_week(week, aday) == ' 6  7  8  9 10 11 12 13 '
    assert str_week(week, bday) == ' 6  7 \x1b[7m 8\x1b[0m  9 10 11 12 13 '


example1 = [
    '\x1b[1m    Mo Tu We Th Fr Sa Su \x1b[0m',
    '\x1b[1mDec \x1b[0m28 29 30  1  2  3  4 ',
    '     5  6  7  8  9 10 11 ',
    '    \x1b[7m12\x1b[0m 13 14 15 16 17 18 ',
    '    19 20 21 22 23 24 25 ',
    '\x1b[1mJan \x1b[0m26 27 28 29 30 31  1 ',
    '     2  3  4  5  6  7  8 ',
    '     9 10 11 12 13 14 15 ',
    '    16 17 18 19 20 21 22 ',
    '    23 24 25 26 27 28 29 ',
    '\x1b[1mFeb \x1b[0m30 31  1  2  3  4  5 ',
    '     6  7  8  9 10 11 12 ',
    '    13 14 15 16 17 18 19 ',
    '    20 21 22 23 24 25 26 ',
    '\x1b[1mMar \x1b[0m27 28 29  1  2  3  4 ']

example_weno = [
    '\x1b[1m    Mo Tu We Th Fr Sa Su     \x1b[0m',
    '\x1b[1mDec \x1b[0m28 29 30  1  2  3  4 \x1b[1m 48\x1b[0m',
    '     5  6  7  8  9 10 11 \x1b[1m 49\x1b[0m',
    '    \x1b[7m12\x1b[0m 13 14 15 16 17 18 \x1b[1m 50\x1b[0m',
    '    19 20 21 22 23 24 25 \x1b[1m 51\x1b[0m',
    '\x1b[1mJan \x1b[0m26 27 28 29 30 31  1 \x1b[1m 52\x1b[0m',
    '     2  3  4  5  6  7  8 \x1b[1m 1\x1b[0m',
    '     9 10 11 12 13 14 15 \x1b[1m 2\x1b[0m',
    '    16 17 18 19 20 21 22 \x1b[1m 3\x1b[0m',
    '    23 24 25 26 27 28 29 \x1b[1m 4\x1b[0m',
    '\x1b[1mFeb \x1b[0m30 31  1  2  3  4  5 \x1b[1m 5\x1b[0m',
    '     6  7  8  9 10 11 12 \x1b[1m 6\x1b[0m',
    '    13 14 15 16 17 18 19 \x1b[1m 7\x1b[0m',
    '    20 21 22 23 24 25 26 \x1b[1m 8\x1b[0m',
    '\x1b[1mMar \x1b[0m27 28 29  1  2  3  4 \x1b[1m 9\x1b[0m']

example_we_start_su = [
    '\x1b[1m    Su Mo Tu We Th Fr Sa \x1b[0m',
    '\x1b[1mDec \x1b[0m27 28 29 30  1  2  3 ',
    '     4  5  6  7  8  9 10 ',
    '    11 \x1b[7m12\x1b[0m 13 14 15 16 17 ',
    '    18 19 20 21 22 23 24 ',
    '    25 26 27 28 29 30 31 ',
    '\x1b[1mJan \x1b[0m 1  2  3  4  5  6  7 ',
    '     8  9 10 11 12 13 14 ',
    '    15 16 17 18 19 20 21 ',
    '    22 23 24 25 26 27 28 ',
    '\x1b[1mFeb \x1b[0m29 30 31  1  2  3  4 ',
    '     5  6  7  8  9 10 11 ',
    '    12 13 14 15 16 17 18 ',
    '    19 20 21 22 23 24 25 ',
    '\x1b[1mMar \x1b[0m26 27 28 29  1  2  3 ']


def test_vertical_month():
    vert_str = vertical_month(month=12, year=2011,
                              today=datetime.date(2011, 12, 12))
    assert vert_str == example1

    weno_str = vertical_month(month=12, year=2011,
                              today=datetime.date(2011, 12, 12),
                              weeknumber=True)
    assert weno_str == example_weno

    we_start_su_str = vertical_month(
        month=12, year=2011,
        today=datetime.date(2011, 12, 12),
        firstweekday=6)
    assert we_start_su_str == example_we_start_su
