from .ColourCode import *

class Logger(object):
    TYPE_KEY = 'type';
    DATA_KEY = 'data';
    COLOUR_KEY = 'colour';
    STRING_KEY = 'string';
    FORMATTER_KEY = 'formatter';
    DISPLAY_KEY = 'display';
    STATE_KEY = 'state';
    
    @classmethod
    def fmt(self, args):
        line = '';
        for item in args:
            item_type = item[Logger.TYPE_KEY];
            item_data = item[Logger.DATA_KEY];
            if item_type == Logger.COLOUR_KEY:
                colour_value = item_data[Logger.COLOUR_KEY];
                state_value = item_data[Logger.STATE_KEY];
                line += ColourCode.lookup(colour_value,state_value);
            elif item_type == Logger.STRING_KEY:
                formatter_value = item_data[Logger.FORMATTER_KEY];
                display_value = item_data[Logger.DISPLAY_KEY];
                line += formatter_value % display_value;
            else:
                line += '';
        
        print line;
    
    @classmethod
    def colour(self, name, state):
        return {
            Logger.TYPE_KEY: Logger.COLOUR_KEY,
            Logger.DATA_KEY: {
                Logger.COLOUR_KEY: name,
                Logger.STATE_KEY: state
            }
        };
    
    @classmethod
    def string(self, formatter, value):
        return {
            Logger.TYPE_KEY: Logger.STRING_KEY,
            Logger.DATA_KEY: {
                Logger.FORMATTER_KEY: formatter,
                Logger.DISPLAY_KEY: value
            }
        };
    
    @classmethod
    def debuglog(cls, args):
        Logger.fmt(args);