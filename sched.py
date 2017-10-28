from qqbot import qqbotsched

@qqbotsched(hour='8', minute='00')
def mytask(bot):
    gl = bot.List('group', '在澳洲搞IT')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, 'G\'day mate!')

