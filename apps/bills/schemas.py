from rest_framework.schemas import AutoSchema
from coreapi import Field, Link, document
import coreschema

class BillSchema(AutoSchema):
  
  def get_link(self, path, method, base_url):
    link = super().get_link(path, method, base_url)

    batch_del_fields = [
      Field('bill_ids', location='body', required=True, schema=coreschema.String(description='账目ID集合'))
    ]

    if link.url == '/api/v1/bills/batch_del/':
      fields = tuple(batch_del_fields)
    else:
      fields = link.fields
    
    link = Link(url=link.url, action=link.action, encoding=link.encoding, fields=fields, description=link.description)
    document.Link()
    return link
