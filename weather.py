{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyP6OwFpky7zUDJLxPqaxQ1v",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/milan136/shape-ai-project-weather.py/blob/main/weather.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6RGUHNdN4f71",
        "outputId": "9231d512-1c81-467f-de6c-dc7228c878fd"
      },
      "source": [
        "import requests\n",
        "import os\n",
        "import sys\n",
        "from datetime import datetime\n",
        "\n",
        "api_key = '28e7c3051cf8db5b3e1c3412353b642e'\n",
        "location = input(\"Enter the city name: \")\n",
        "\n",
        "complete_api_link = \"https://api.openweathermap.org/data/2.5/weather?q=\"+location+\"&appid=\"+api_key\n",
        "api_link = requests.get(complete_api_link)\n",
        "api_data = api_link.json()\n",
        "\n",
        "\n",
        "temp_city = ((api_data['main']['temp'])-273.15)\n",
        "weather_desc = api_data['weather'][0]['description']\n",
        "hmdt = api_data['main']['humidity']\n",
        "wind_spd = api_data['wind']['speed']\n",
        "date_time = datetime.now().strftime(\"%d %b %Y | %I:%M:%S %p\")\n",
        "\n",
        "print (\"-------------------------------------------------------------\")\n",
        "print (\"Weather Stats for - {}  || {}\".format(location.upper(), date_time))\n",
        "print (\"-------------------------------------------------------------\")\n",
        "\n",
        "print (\"Current temperature is: {:.2f} °C\".format(temp_city))\n",
        "print (\"Current weather desc  :\",weather_desc)\n",
        "print (\"Current Humidity      :\",hmdt, '%')\n",
        "print (\"Current wind speed    :\",wind_spd ,'kmph')\n",
        "\n",
        "\n",
        "data={'city':location,\n",
        "      'date & time':date_time,\n",
        "      'temp(°C)':temp_city,\n",
        "      'weather desc':weather_desc,\n",
        "      'humidity':hmdt,\n",
        "      'wind(kmph)':wind_spd}\n",
        "\n",
        "\n",
        "file = open(\"Data.txt\", \"a\")\n",
        "str_data= repr(data)\n",
        "file.write(\"Data = \" + str_data + \"\\n\")\n",
        "file.close()\n",
        "\n",
        "\n",
        "x=input(\"\\nDo you want to see all the search history(Y/N): \")\n",
        "if x=='y' or x=='Y':\n",
        "  with open(\"Data.txt\",\"r\") as fp:\n",
        "    print(fp.read())\n",
        "  z=input(\"Do you want to delete all search history(Y/N): \")\n",
        "  if z=='y' or z=='Y':\n",
        "    f = open(\"Data.txt\",\"w\")\n",
        "    f.truncate()\n",
        "    f.close()\n",
        "    print('Search history successfuly cleard')\n",
        "  else:\n",
        "    sys.exit(\"Successful termination\")   \n",
        "else:\n",
        "  sys.exit(\"Successful termination\")"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the city name: pala\n",
            "-------------------------------------------------------------\n",
            "Weather Stats for - PALA  || 23 Jun 2021 | 08:04:38 AM\n",
            "-------------------------------------------------------------\n",
            "Current temperature is: 21.84 °C\n",
            "Current weather desc  : overcast clouds\n",
            "Current Humidity      : 89 %\n",
            "Current wind speed    : 5.28 kmph\n",
            "\n",
            "Do you want to see all the search history(Y/N): y\n",
            "Data = {'city': 'pala', 'date & time': '23 Jun 2021 | 08:04:38 AM', 'temp(°C)': 21.840000000000032, 'weather desc': 'overcast clouds', 'humidity': 89, 'wind(kmph)': 5.28}\n",
            "\n",
            "Do you want to delete all search history(Y/N): y\n",
            "Search history successfuly cleard\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}