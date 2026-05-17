#!/usr/bin/env python3
import json, zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BASE = REPO / 'power-automate' / 'procedimiento-package'
FLOW_ID = '8f5d4e25-6d62-4b75-a4f3-7f7e2a8f91d1'
PUBLISHER_ID = '2b4c63a2-8e6d-4f11-8fb3-37b4a2893b62'

manifest = {
  'name': 'Procedimiento',
  'description': 'Paquete base importable para Power Automate: revisión + aprobación + publicación en SharePoint.',
  'schemaVersion': '1.0.0.0',
  'packageFormat': 'zip',
  'publisher': {'displayName': 'Maxxuel Smart', 'id': PUBLISHER_ID},
  'creationTime': '2026-05-17T22:05:00Z',
  'resources': [{
    'resourceName': FLOW_ID,
    'resourceType': 'Microsoft.Flow/flows',
    'resourcePath': f'Microsoft.Flow/flows/{FLOW_ID}/definition.json',
    'details': {
      'displayName': 'Procedimiento',
      'description': 'Flujo base con revisor, aprobador y publicación final en SharePoint.',
      'createdTime': '2026-05-17T22:05:00Z',
      'lastModifiedTime': '2026-05-17T22:05:00Z'
    },
    'connectionReferences': {
      'shared_sharepointonline': {'runtimeSource': 'embedded', 'connection': {'connectionReferenceLogicalName': 'crd_shared_sharepointonline'}, 'api': {'name': 'shared_sharepointonline'}},
      'shared_approvals': {'runtimeSource': 'embedded', 'connection': {'connectionReferenceLogicalName': 'crd_shared_approvals'}, 'api': {'name': 'shared_approvals'}},
      'shared_office365': {'runtimeSource': 'embedded', 'connection': {'connectionReferenceLogicalName': 'crd_shared_office365'}, 'api': {'name': 'shared_office365'}}
    }
  }]
}

definition_path = BASE / 'Microsoft.Flow' / 'flows' / FLOW_ID / 'definition.json'
connections_path = BASE / 'connections.json'
readme_path = BASE / 'README.md'
manifest_path = BASE / 'manifest.json'

definition = json.loads(definition_path.read_text(encoding='utf-8'))
connections = json.loads(connections_path.read_text(encoding='utf-8'))
readme = readme_path.read_text(encoding='utf-8')

manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding='utf-8')
connections_path.write_text(json.dumps(connections, indent=2, ensure_ascii=False) + "\n", encoding='utf-8')
definition_path.write_text(json.dumps(definition, indent=2, ensure_ascii=False) + "\n", encoding='utf-8')
readme_path.write_text(readme, encoding='utf-8')

zip_path = BASE / 'Procedimiento-import.zip'
with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for path in BASE.rglob('*'):
        if path.is_file() and path.name != 'Procedimiento-import.zip':
            z.write(path, path.relative_to(BASE))
print(zip_path)
