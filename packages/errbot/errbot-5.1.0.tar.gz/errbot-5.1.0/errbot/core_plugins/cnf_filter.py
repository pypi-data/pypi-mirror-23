from errbot import BotPlugin, cmdfilter


class CommandNotFoundFilter(BotPlugin):
    @cmdfilter(catch_unprocessed=True)
    def cnf_filter(self, msg, cmd, args, dry_run, emptycmd=False):
        """
        Check if command exists.  If not, signal plugins.  This plugin
        will be called twice: once as a command filter and then again
        as a "command not found" filter. See the emptycmd parameter.

        :param msg: Original chat message.
        :param cmd: Parsed command.
        :param args: Command arguments.
        :param dry_run: True when this is a dry-run.
        :param emptycmd: False when this command has been parsed and is valid.
        True if the command was not found.
        """

        if not emptycmd:
            return msg, cmd, args

        if self.bot_config.SUPPRESS_CMD_NOT_FOUND:
            self.log.debug("Suppressing command not found feedback")
        else:
            if msg.body.find(' ') > 0:
                command = msg.body[:msg.body.index(' ')]
            else:
                command = msg.body

            prefixes = self.bot_config.BOT_ALT_PREFIXES + (self.bot_config.BOT_PREFIX,)
            for prefix in prefixes:
                if command.startswith(prefix):
                    command = command.replace(prefix, '', 1)
                    break

            reply = self._bot.unknown_command(msg, command, args)
            if reply is None:
                reply = self.MSG_UNKNOWN_COMMAND % {'command': cmd}
            if reply:
                return reply
