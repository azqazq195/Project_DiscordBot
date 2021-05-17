# @client.event
# async def on_member_join(member):
#     print(f'{member} has joined a server.')


# @client.event
# async def on_member_remove(member):
#     print(f'{member} has left a server.')


# @client.command()
# async def clear(ctx, amount=5):
#     await ctx.channel.purge(limit=amount)


# @client.command()
# async def kick(ctx, member: discord.Member, *, reason=None):
#     await member.kick(reason=reason)


# @client.command()
# async def ban(ctx, member: discord.Member, *, reason=None):
#     await member.ban(reason=reason)
#     await ctx.send(f'Banned {member.mention}')


# @client.command()
# async def unban(ctx, *, member):
#     banned_users = await ctx.guild.bans()
#     member_name, member_discriminator = member.split('#')
#
#     for ban_entry in banned_users:
#         user = ban_entry.user
#
#         if(user.name, user.discriminator) == (member_name, member_discriminator):
#             await ctx.guild.unban(user)
#             await ctx.send(f'Unbanned {user.mention}')
#             return