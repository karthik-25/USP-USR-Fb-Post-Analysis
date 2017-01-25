import json



s = '''
{
  "data": [
    {
      "message": "Death by fatty liver disease: Research led by Prof Koh Woon Puay from Duke-NUS Medical School and NUS Saw Swee Hock School of Public Health suggests its link to diabetes. Non-alcoholic fatty liver disease is also even more fatal to LEAN diabetics than their overweight counterparts! #NUSResearch :O",
      "created_time": "2017-01-24T23:30:00+0000",
      "id": "176017608539_10154948281633540"
    },
    {
      "message": "Duke-NUS Medical School researchers uncover a possible link between #autism and mutations in the gene CDH13, which affects communications between brain cells! #NUSResearch",
      "created_time": "2017-01-24T09:30:00+0000",
      "id": "176017608539_10154947369638540"
    },
    {
      "message": "Kudos to the NUS Kendo Club for hosting the 6th Inter-Club Kendo Tournament over the weekend! This tournament is the largest Kendo tournament in Singapore with over 250 matches fought across 2 days! #NUSLife",
      "story": "National University of Singapore added 6 new photos.",
      "created_time": "2017-01-23T23:30:00+0000",
      "id": "176017608539_10154944316498540"
    }
  ],
  "paging": {
    "previous": "https://graph.facebook.com/v2.8/176017608539/feed?format=json&since=1485300600&access_token=EAACEdEose0cBAFjy2ZAj71heO1XeidAC7SBulciDEPoj1jk7DWQE2Y99l385BPXSoeCdDlZAZBqhKGUTtFiNCDDZB0R7hoIuIFmRxsR7wJSZCZAggM29jJA8yNtFXZBWWWya9mKLXjJdZAclGzjLmRPjzpR7QFmbDY8MEUnbv4M9LQZDZD&limit=25&__paging_token=enc_AdD7HgPDipclHhGVdTPwCds4slEnISqaGFATbq18iHt2ZAZCRkTiZBkB4fd9RK11vHAvFAjEr3dvBqJ3D5Jl2xAfr3w5OvhnxsBsFTPsoZBz8fkpxQZDZD&__previous=1",
    "next": "https://graph.facebook.com/v2.8/176017608539/feed?format=json&access_token=EAACEdEose0cBAFjy2ZAj71heO1XeidAC7SBulciDEPoj1jk7DWQE2Y99l385BPXSoeCdDlZAZBqhKGUTtFiNCDDZB0R7hoIuIFmRxsR7wJSZCZAggM29jJA8yNtFXZBWWWya9mKLXjJdZAclGzjLmRPjzpR7QFmbDY8MEUnbv4M9LQZDZD&limit=25&until=1484352257&__paging_token=enc_AdCnea2bNzoUCjZALmXIZAwIZBLgXArRFEhyXxv5mYPi3BSdKd9hRuOJtkdNTy17c3s6cwmYuZCqd3y66p0yNUbFcjWySzbTU1ZBh7gmwgmvX3GWq0wZDZD"
  }
}
'''


j = json.loads(s)
for x in j['data']:
  print x["message"]

  