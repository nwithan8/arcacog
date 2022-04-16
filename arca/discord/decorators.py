from functools import wraps

from dbotbase.discord_utils import user_is_admin, send_error, disable_exception_traceback, PermissionAbuseWarning


# Custom decorators

def is_admin(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        cog = args[0]
        ctx = args[1]
        if await user_is_admin(cog=cog, ctx=ctx):
            return await func(*args, **kwargs)
        await send_error(ctx=ctx, error_message="You are not an admin!")
        with disable_exception_traceback():
            raise PermissionAbuseWarning(user_name=ctx.author.name)

    return inner
