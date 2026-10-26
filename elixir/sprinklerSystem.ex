# Sprinkler system in Elixir
# Compiled binary can run at specific intervals, assumption > code exec every hour

defmodule Sprinkler do

    def fetchWeatherDetails() do

    end

    def run do

        # fetch weather information from Open weather
        fetchWeatherDetails()

        # log weather information into log file

        # clear log file every 1st of each month when log lines > 2000 lines

        # check logs for rain. Calculate mean; will determine if lawn sprinkler needs to run

        # run sprinkler if forcasted rain is not detected and if logs have no sign of rain. Need
        # to ensure that the mean is accurate enough to predict soil wetness.

        # send GPIO output to run water. end after the provided time in the config.

    end

end
