# sosaxy [![Build Status](https://travis-ci.org/xianwill/py-sosaxy.svg?branch=master)](https://travis-ci.org/xianwill/py-sosaxy)

a utility for doing simple transformations on xml using `xml.sax` as the underlying parser.

## installation

```
pip3 install sosaxy
```

## doing simple transforms

`RecordStream` is the main workhorse... import it:

```
from sosaxy import RecordStream
```

create an instance of `RecordStream` giving it a 

* file name to parse or a StringIO instance containing xml.
* the record boundary element name for your xml - in the example below - this is `record`
* the fields you want to pull
* your record handler function - the example just uses `print`

```
rs = RecordStream('myfile.xml', 'record', ['record/@attr1', 'record/elem', 'record/elem/@eattr1'], print)
```

the instantiation described above is designed to handle the xml shown below:

```
<records>
  <record attr1="a">
    <elem eattr1="p">some content</elem>
  </record>
</records>
```

run `play` to start the stream

```
rs.play()
```

this will emit the output below:

```
{'attr1': 'a', 'elem': {'text': 'some content', 'eattr1': 'p'}}
```

## command line

the x2j command line utility is a great way to just dump straight to a new-line delimited file.

```
sosaxy x2j $SCRIPTPATH/../resources/test.xml $SCRIPTPATH/../data/test.json record record/elem record/@attr record/elem/@eattr
```
