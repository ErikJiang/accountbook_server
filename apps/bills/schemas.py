from rest_framework.schemas import AutoSchema
from coreapi import Field, Link, document
import coreschema

class BillSchema(AutoSchema):
  
  def get_link(self, path, method, base_url):
    link = super().get_link(path, method, base_url)
    # 无法指定bill_ids数组中的元素类型，这里元素定义为int但实际为str，无法处理...
    batch_del_fields = [
      Field(
        'bill_ids', 
        location='form', 
        required=True,
        schema=coreschema.Array(items=coreschema.Integer(),unique_items=True)
      )
    ]
    fields = link.fields
    if link.url == '/api/v1/bills/batch/' and method.lower() == 'delete':
      fields = tuple(batch_del_fields)
    
    link = Link(url=link.url, action=link.action, encoding=link.encoding, fields=fields, description=link.description)
    document.Link()
    return link
