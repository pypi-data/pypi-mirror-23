#ifndef LISTENER_H
#define LISTENER_H
#include "Python.h"
#include "orientc_reader.h"
#include <stack>

using namespace Orient;
using namespace std;

class TrackerListener: public RecordParseListener {
 public:
  PyObject *obj;
  string *cur_field;
  stack<OType> types_stack;
  stack<PyObject*> obj_stack;

  
  virtual void startDocument(const char * name,size_t name_length) ;
  virtual void endDocument() ;
  virtual void startField(const char * name,size_t name_length, OType type) ;
  virtual void endField(const char * name,size_t name_length) ;
  virtual void stringValue(const char * value,size_t value_length) ;
  virtual void intValue(long value) ;
  virtual void longValue(long long value) ;
  virtual void shortValue(short value);
  virtual void byteValue(char value) ;
  virtual void booleanValue(bool value);
  virtual void floatValue(float value) ;
  virtual void doubleValue(double value) ;
  virtual void binaryValue(const char * value, int length) ;
  virtual void dateValue(long long value) ;
  virtual void dateTimeValue(long long value) ;
  virtual void linkValue(struct Link &value) ;
  virtual void startCollection(int size,OType type);
  virtual void startMap(int size,OType type) ;
  virtual void mapKey(const char *key,size_t key_length);
  virtual void ridBagTreeKey(long long fileId,long long pageIndex,long pageOffset);
  virtual void nullValue();
  virtual void endMap(OType type);
  virtual void endCollection(OType type);
  virtual void decimalValue(int scale , const char * bytes, int bytes_length);
  
  TrackerListener(PyObject* props) ;
  ~TrackerListener() ;

};

#endif
