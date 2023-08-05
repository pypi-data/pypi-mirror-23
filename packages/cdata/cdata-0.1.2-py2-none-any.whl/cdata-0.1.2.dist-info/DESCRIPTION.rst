cdata
-------------

"see data", see data, handy snippets for conversion, cleaning and integration.


json data manipulation
-------------

* json (and json stream) file IO, e.g.  items2file(...)
* json data access, e.g. json_get(...)
* json array statistics, e.g. stat(...)

.. code-block:: python

  from cdata.core import any2utf8
  the_input = {"hello": u"世界"}
  the_output = any2utf8(the_input)
  logging.info((the_input, the_output))


table data manipulation
-------------

* json array to/from excel

.. code-block:: python

  import json
  from cdata.table import excel2json,json2excel
  filename = "test.xls"
  items = [{"first":"hello", "last":"world" }]
  json2excel(items, ["first","last"], filename)
  ret = excel2json(filename)
  print json.dumps(ret)



JSON data from reading a single sheet excel file

.. code-block:: json

  {
    "fields": {
        "00": [
            "name",
            "年龄",
            "notes"
        ]
    },
    "data": {
        "00": [
            {
                "notes": "",
                "年龄": 18.0,
                "name": "张三"
            },
            {
                "notes": "this is li si",
                "年龄": 18.0,
                "name": "李四"
            }
        ]
    }
  }

web stuff
-------------

* url domain extraction

entity manipulation
-------------

* entity.SimpleEntity.ner()

.. code-block:: python

  from cdata.entity import SimpleEntity
  entity_list = [{"@id":"1","name":u"张三"},{"@id":"2","name":u"李四"}]
  ner = SimpleEntity(entity_list)
  sentence = "张三给了李四一个苹果"
  ret = ner.ner(sentence)
  logging.info(json.dumps(ret, ensure_ascii=False, indent=4))
  """
  [{
      "text": "张三",
      "entities": [
          {
              "@id": "1",
              "name": "张三"
          }
      ],
      "index": 0
  },
  {
      "text": "李四",
      "entities": [
          {
              "@id": "2",
              "name": "李四"
          }
      ],
      "index": 4
  }]
  """

* region.RegionEntity.guess_all()

.. code-block:: python

  from cdata.region import RegionEntity
  addresses = ["北京海淀区阜成路52号（定慧寺）", "北京大学肿瘤医院"]

  result = city_data.guess_all(addresses)
  logging.info(json.dumps(result, ensure_ascii=False))
  """
     {"province": "北京市",
     "city": "市辖区",
     "name": "海淀区",
     "district": "海淀区",
     "cityid": "110108",
     "type": "district"}
  """
misc
-------------

* support simple cli function using argparse


