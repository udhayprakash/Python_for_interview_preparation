import json
import urllib.request


def getTopRatedFoodOutlets(city):
    outlets = []
    pageNumber = 1
    ratings = {}
    maxRating = 0
    while True:
        URL = f"https://jsonmock.hackerrank.com/api/food_outlets?city={city}&page={pageNumber}"
        response = urllib.request.urlopen(URL)
        data = json.loads(response.read())

        for each in data["data"]:
            currRating = each["user_rating"]["average_rating"]
            ratings.setdefault(currRating, [])
            ratings[currRating].append(each["name"])
            if currRating > maxRating:
                maxRating = currRating
        if data["page"] == data["total_pages"]:
            break
        pageNumber += 1

    return ratings[maxRating]


if __name__ == "__main__":
    assert getTopRatedFoodOutlets("Denver") == [
        "Sushi Kashiba",
        "Peninsula Grand Hotel",
        "Plum by Bent Chair",
        "R' ADDA",
        "Palladium Social",
    ]
    assert getTopRatedFoodOutlets("Houston") == ["Barbeque Nation"]
    assert getTopRatedFoodOutlets("Seattle") == [
        "Cafe Juanita",
        "Cafe Munir",
        "Asia Kitchen By Mainland China",
        "AB's - Absolute Barbecues",
    ]
    assert getTopRatedFoodOutlets("Miami") == ["Decode Air Bar"]
    assert getTopRatedFoodOutlets("Omaha") == [
        "The Saffron Tree",
        "Echoes Omaha",
        "Barbeque Nation",
    ]
    assert getTopRatedFoodOutlets("Dallas") == [
        "Coal Barbecues",
        "Coal Barbecues",
        "AB's - Absolute Barbecues",
        "AB's - Absolute Barbecues",
        "AB's - Absolute Barbecues",
        "AB's - Absolute Barbecues",
        "Bateau",
    ]
    assert getTopRatedFoodOutlets("Boston") == ["Uncle Jack's"]
