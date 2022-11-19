"""
Problem: Vaidate braces in Json string
"""

json = """
{
  "took": 7,
  "timed_out": false,
  "_shards": {
    "total": 3,
    "successful": 3,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 10000,
      "relation": "gte"
    },
    "max_score": 2.8592248,
    "hits": [
      {
        "_index": "metadata-summary-2022.09",
        "_type": "_doc",
        "_id": "M0SV-4IBgIhLnOQNcXW9",
        "_score": 2.8592248,
        "_source": {
          "delivered": true,
          "created": "2022-09-02T00:24:11.451536+00:00",
          "job_uuid": "ed1855bb829f47feb408e12a39d4279d",
          "team": "foo",
          "job_type": "eng",
          "build_environment": "production",
          "partition": "default",
          "event_source": "bo",
          "job_name": "foo-20E_main-ios-buildit-eng-MarkE-bar",
          "build_number": 2,
          "execution_target": "rno-c3",
          "build_type": "buildit",
          "xbs_project": "bar",
          "branch": "20E_main",
          "train": "MarkE",
          "platform": "ios",
          "events": {
            "install_xia": {
              "inconsistent": false,
              "start": "2022-09-02T00:19:33.944236+00:00",
              "end": "2022-09-02T00:24:03.181050+00:00",
              "duration": 269.236814
            },
            "job": {
              "inconsistent": false,
              "end": "2022-09-02T00:24:04.873768+00:00",
              "start": "2022-09-02T00:19:27.490033+00:00",
              "duration": 277.383735
            }
          },
          "messages": {
            "locate_xia_in_local_cache|job": "Verify mage on local storage",
            "start|install_xia": "Intalling image",
            "end|install_xia": "Intalling image",
            "artifact_url|job": "Get artifactory download path"
          },
          "inconsistent": false
        }
      ]
    ]
  }
}
"""


class JsonValidator:
    def __init__(self):
        self.braces_pair = {"}": "{", "]": "[", ")": "("}

    def is_valid(self, json_str):
        braces_found = []
        line_count = 0
        for index, each_chr in enumerate(json_str):
            if each_chr in ("{", "}", "[", "]"):  # open/close braces
                line_count += 1
            elif each_chr == ",":
                # As before line too, as it wont have close braces
                line_count += 2 if json_str[index - 1] in "]}" else 1

            if each_chr in self.braces_pair.values():
                braces_found.append(each_chr)
            elif each_chr in self.braces_pair:
                exitsng_brace = braces_found.pop()
                curr_brace = self.braces_pair[each_chr]
                if (not braces_found) or exitsng_brace != curr_brace:
                    return False, line_count, (exitsng_brace, curr_brace)
        return False if braces_found else True


jv = JsonValidator()
print(jv.is_valid(json))
