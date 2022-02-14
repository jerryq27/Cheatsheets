#include <iostream>

static int s_Variable = 5;

class Log {
public:
    enum Level {
        LevelError, LevelWarning, LevelInfo
    };

private:
    Level m_LogLevel = LevelInfo;

public:
    void setLevel(Level level) {
        m_LogLevel = level;
    }

    void error(const char* message) {
        if(m_LogLevel >= LevelError)
            std::cout << "[ERROR]: " << message << std::endl;
    }

    void warn(const char* message) {
        if(m_LogLevel >= LevelWarning)
            std::cout << "[WARNING]: " << message << std::endl;
    }

    void info(const char* message) {
        if(m_LogLevel >= LevelInfo)
            std::cout << "[INFO]: " << message << std::endl;
    }
};

int main() {
    Log log;
    log.setLevel(Log::LevelError);
    log.error("OH NOEZ");
    log.warn("Hello!");
    log.info("What's up?!");
}