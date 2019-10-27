"""Generated client library for firestore version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.firestore.v1 import firestore_v1_messages as messages


class FirestoreV1(base_api.BaseApiClient):
  """Generated client library for service firestore version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://firestore.googleapis.com/'

  _PACKAGE = u'firestore'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/datastore']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'FirestoreV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new firestore handle."""
    url = url or self.BASE_URL
    super(FirestoreV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_databases_collectionGroups_fields = self.ProjectsDatabasesCollectionGroupsFieldsService(self)
    self.projects_databases_collectionGroups_indexes = self.ProjectsDatabasesCollectionGroupsIndexesService(self)
    self.projects_databases_collectionGroups = self.ProjectsDatabasesCollectionGroupsService(self)
    self.projects_databases_documents = self.ProjectsDatabasesDocumentsService(self)
    self.projects_databases_operations = self.ProjectsDatabasesOperationsService(self)
    self.projects_databases = self.ProjectsDatabasesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsDatabasesCollectionGroupsFieldsService(base_api.BaseApiService):
    """Service class for the projects_databases_collectionGroups_fields resource."""

    _NAME = u'projects_databases_collectionGroups_fields'

    def __init__(self, client):
      super(FirestoreV1.ProjectsDatabasesCollectionGroupsFieldsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the metadata and configuration for a Field.

      Args:
        request: (FirestoreProjectsDatabasesCollectionGroupsFieldsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleFirestoreAdminV1Field) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/collectionGroups/{collectionGroupsId}/fields/{fieldsId}',
        http_method=u'GET',
        method_id=u'firestore.projects.databases.collectionGroups.fields.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'FirestoreProjectsDatabasesCollectionGroupsFieldsGetRequest',
        response_type_name=u'GoogleFirestoreAdminV1Field',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists the field configuration and metadata for this database.

Currently, FirestoreAdmin.ListFields only supports listing fields
that have been explicitly overridden. To issue this query, call
FirestoreAdmin.ListFields with the filter set to
`indexConfig.usesAncestorConfig:false`.

      Args:
        request: (FirestoreProjectsDatabasesCollectionGroupsFieldsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleFirestoreAdminV1ListFieldsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/collectionGroups/{collectionGroupsId}/fields',
        http_method=u'GET',
        method_id=u'firestore.projects.databases.collectionGroups.fields.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+parent}/fields',
        request_field='',
        request_type_name=u'FirestoreProjectsDatabasesCollectionGroupsFieldsListRequest',
        response_type_name=u'GoogleFirestoreAdminV1ListFieldsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a field configuration. Currently, field updates apply only to.
single field index configuration. However, calls to
FirestoreAdmin.UpdateField should provide a field mask to avoid
changing any configuration that the caller isn't aware of. The field mask
should be specified as: `{ paths: "index_config" }`.

This call returns a google.longrunning.Operation which may be used to
track the status of the field update. The metadata for
the operation will be the type FieldOperationMetadata.

To configure the default field settings for the database, use
the special `Field` with resource name:
`projects/{project_id}/databases/{database_id}/collectionGroups/__default__/fields/*`.

      Args:
        request: (FirestoreProjectsDatabasesCollectionGroupsFieldsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/collectionGroups/{collectionGroupsId}/fields/{fieldsId}',
        http_method=u'PATCH',
        method_id=u'firestore.projects.databases.collectionGroups.fields.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1/{+name}',
        request_field=u'googleFirestoreAdminV1Field',
        request_type_name=u'FirestoreProjectsDatabasesCollectionGroupsFieldsPatchRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsDatabasesCollectionGroupsIndexesService(base_api.BaseApiService):
    """Service class for the projects_databases_collectionGroups_indexes resource."""

    _NAME = u'projects_databases_collectionGroups_indexes'

    def __init__(self, client):
      super(FirestoreV1.ProjectsDatabasesCollectionGroupsIndexesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a composite index. This returns a google.longrunning.Operation.
which may be used to track the status of the creation. The metadata for
the operation will be the type IndexOperationMetadata.

      Args:
        request: (FirestoreProjectsDatabasesCollectionGroupsIndexesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/collectionGroups/{collectionGroupsId}/indexes',
        http_method=u'POST',
        method_id=u'firestore.projects.databases.collectionGroups.indexes.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}/indexes',
        request_field=u'googleFirestoreAdminV1Index',
        request_type_name=u'FirestoreProjectsDatabasesCollectionGroupsIndexesCreateRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a composite index.

      Args:
        request: (FirestoreProjectsDatabasesCollectionGroupsIndexesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/collectionGroups/{collectionGroupsId}/indexes/{indexesId}',
        http_method=u'DELETE',
        method_id=u'firestore.projects.databases.collectionGroups.indexes.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'FirestoreProjectsDatabasesCollectionGroupsIndexesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a composite index.

      Args:
        request: (FirestoreProjectsDatabasesCollectionGroupsIndexesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleFirestoreAdminV1Index) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/collectionGroups/{collectionGroupsId}/indexes/{indexesId}',
        http_method=u'GET',
        method_id=u'firestore.projects.databases.collectionGroups.indexes.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'FirestoreProjectsDatabasesCollectionGroupsIndexesGetRequest',
        response_type_name=u'GoogleFirestoreAdminV1Index',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists composite indexes.

      Args:
        request: (FirestoreProjectsDatabasesCollectionGroupsIndexesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleFirestoreAdminV1ListIndexesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/collectionGroups/{collectionGroupsId}/indexes',
        http_method=u'GET',
        method_id=u'firestore.projects.databases.collectionGroups.indexes.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+parent}/indexes',
        request_field='',
        request_type_name=u'FirestoreProjectsDatabasesCollectionGroupsIndexesListRequest',
        response_type_name=u'GoogleFirestoreAdminV1ListIndexesResponse',
        supports_download=False,
    )

  class ProjectsDatabasesCollectionGroupsService(base_api.BaseApiService):
    """Service class for the projects_databases_collectionGroups resource."""

    _NAME = u'projects_databases_collectionGroups'

    def __init__(self, client):
      super(FirestoreV1.ProjectsDatabasesCollectionGroupsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsDatabasesDocumentsService(base_api.BaseApiService):
    """Service class for the projects_databases_documents resource."""

    _NAME = u'projects_databases_documents'

    def __init__(self, client):
      super(FirestoreV1.ProjectsDatabasesDocumentsService, self).__init__(client)
      self._upload_configs = {
          }

    def BatchGet(self, request, global_params=None):
      r"""Gets multiple documents.

Documents returned by this method are not guaranteed to be returned in the
same order that they were requested.

      Args:
        request: (FirestoreProjectsDatabasesDocumentsBatchGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BatchGetDocumentsResponse) The response message.
      """
      config = self.GetMethodConfig('BatchGet')
      return self._RunMethod(
          config, request, global_params=global_params)

    BatchGet.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/documents:batchGet',
        http_method=u'POST',
        method_id=u'firestore.projects.databases.documents.batchGet',
        ordered_params=[u'database'],
        path_params=[u'database'],
        query_params=[],
        relative_path=u'v1/{+database}/documents:batchGet',
        request_field=u'batchGetDocumentsRequest',
        request_type_name=u'FirestoreProjectsDatabasesDocumentsBatchGetRequest',
        response_type_name=u'BatchGetDocumentsResponse',
        supports_download=False,
    )

    def BeginTransaction(self, request, global_params=None):
      r"""Starts a new transaction.

      Args:
        request: (FirestoreProjectsDatabasesDocumentsBeginTransactionRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BeginTransactionResponse) The response message.
      """
      config = self.GetMethodConfig('BeginTransaction')
      return self._RunMethod(
          config, request, global_params=global_params)

    BeginTransaction.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/documents:beginTransaction',
        http_method=u'POST',
        method_id=u'firestore.projects.databases.documents.beginTransaction',
        ordered_params=[u'database'],
        path_params=[u'database'],
        query_params=[],
        relative_path=u'v1/{+database}/documents:beginTransaction',
        request_field=u'beginTransactionRequest',
        request_type_name=u'FirestoreProjectsDatabasesDocumentsBeginTransactionRequest',
        response_type_name=u'BeginTransactionResponse',
        supports_download=False,
    )

    def Commit(self, request, global_params=None):
      r"""Commits a transaction, while optionally updating documents.

      Args:
        request: (FirestoreProjectsDatabasesDocumentsCommitRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CommitResponse) The response message.
      """
      config = self.GetMethodConfig('Commit')
      return self._RunMethod(
          config, request, global_params=global_params)

    Commit.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/documents:commit',
        http_method=u'POST',
        method_id=u'firestore.projects.databases.documents.commit',
        ordered_params=[u'database'],
        path_params=[u'database'],
        query_params=[],
        relative_path=u'v1/{+database}/documents:commit',
        request_field=u'commitRequest',
        request_type_name=u'FirestoreProjectsDatabasesDocumentsCommitRequest',
        response_type_name=u'CommitResponse',
        supports_download=False,
    )

    def CreateDocument(self, request, global_params=None):
      r"""Creates a new document.

      Args:
        request: (FirestoreProjectsDatabasesDocumentsCreateDocumentRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Document) The response message.
      """
      config = self.GetMethodConfig('CreateDocument')
      return self._RunMethod(
          config, request, global_params=global_params)

    CreateDocument.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/documents/{documentsId}/{collectionId}',
        http_method=u'POST',
        method_id=u'firestore.projects.databases.documents.createDocument',
        ordered_params=[u'parent', u'collectionId'],
        path_params=[u'collectionId', u'parent'],
        query_params=[u'documentId', u'mask_fieldPaths'],
        relative_path=u'v1/{+parent}/{collectionId}',
        request_field=u'document',
        request_type_name=u'FirestoreProjectsDatabasesDocumentsCreateDocumentRequest',
        response_type_name=u'Document',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a document.

      Args:
        request: (FirestoreProjectsDatabasesDocumentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/documents/{documentsId}/{documentsId1}',
        http_method=u'DELETE',
        method_id=u'firestore.projects.databases.documents.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'currentDocument_exists', u'currentDocument_updateTime'],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'FirestoreProjectsDatabasesDocumentsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a single document.

      Args:
        request: (FirestoreProjectsDatabasesDocumentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Document) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/documents/{documentsId}/{documentsId1}',
        http_method=u'GET',
        method_id=u'firestore.projects.databases.documents.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'mask_fieldPaths', u'readTime', u'transaction'],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'FirestoreProjectsDatabasesDocumentsGetRequest',
        response_type_name=u'Document',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists documents.

      Args:
        request: (FirestoreProjectsDatabasesDocumentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDocumentsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/documents/{documentsId}/{documentsId1}/{collectionId}',
        http_method=u'GET',
        method_id=u'firestore.projects.databases.documents.list',
        ordered_params=[u'parent', u'collectionId'],
        path_params=[u'collectionId', u'parent'],
        query_params=[u'mask_fieldPaths', u'orderBy', u'pageSize', u'pageToken', u'readTime', u'showMissing', u'transaction'],
        relative_path=u'v1/{+parent}/{collectionId}',
        request_field='',
        request_type_name=u'FirestoreProjectsDatabasesDocumentsListRequest',
        response_type_name=u'ListDocumentsResponse',
        supports_download=False,
    )

    def ListCollectionIds(self, request, global_params=None):
      r"""Lists all the collection IDs underneath a document.

      Args:
        request: (FirestoreProjectsDatabasesDocumentsListCollectionIdsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListCollectionIdsResponse) The response message.
      """
      config = self.GetMethodConfig('ListCollectionIds')
      return self._RunMethod(
          config, request, global_params=global_params)

    ListCollectionIds.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/documents/{documentsId}/{documentsId1}:listCollectionIds',
        http_method=u'POST',
        method_id=u'firestore.projects.databases.documents.listCollectionIds',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}:listCollectionIds',
        request_field=u'listCollectionIdsRequest',
        request_type_name=u'FirestoreProjectsDatabasesDocumentsListCollectionIdsRequest',
        response_type_name=u'ListCollectionIdsResponse',
        supports_download=False,
    )

    def Listen(self, request, global_params=None):
      r"""Listens to changes.

      Args:
        request: (FirestoreProjectsDatabasesDocumentsListenRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListenResponse) The response message.
      """
      config = self.GetMethodConfig('Listen')
      return self._RunMethod(
          config, request, global_params=global_params)

    Listen.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/documents:listen',
        http_method=u'POST',
        method_id=u'firestore.projects.databases.documents.listen',
        ordered_params=[u'database'],
        path_params=[u'database'],
        query_params=[],
        relative_path=u'v1/{+database}/documents:listen',
        request_field=u'listenRequest',
        request_type_name=u'FirestoreProjectsDatabasesDocumentsListenRequest',
        response_type_name=u'ListenResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates or inserts a document.

      Args:
        request: (FirestoreProjectsDatabasesDocumentsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Document) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/documents/{documentsId}/{documentsId1}',
        http_method=u'PATCH',
        method_id=u'firestore.projects.databases.documents.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'currentDocument_exists', u'currentDocument_updateTime', u'mask_fieldPaths', u'updateMask_fieldPaths'],
        relative_path=u'v1/{+name}',
        request_field=u'document',
        request_type_name=u'FirestoreProjectsDatabasesDocumentsPatchRequest',
        response_type_name=u'Document',
        supports_download=False,
    )

    def Rollback(self, request, global_params=None):
      r"""Rolls back a transaction.

      Args:
        request: (FirestoreProjectsDatabasesDocumentsRollbackRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Rollback')
      return self._RunMethod(
          config, request, global_params=global_params)

    Rollback.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/documents:rollback',
        http_method=u'POST',
        method_id=u'firestore.projects.databases.documents.rollback',
        ordered_params=[u'database'],
        path_params=[u'database'],
        query_params=[],
        relative_path=u'v1/{+database}/documents:rollback',
        request_field=u'rollbackRequest',
        request_type_name=u'FirestoreProjectsDatabasesDocumentsRollbackRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def RunQuery(self, request, global_params=None):
      r"""Runs a query.

      Args:
        request: (FirestoreProjectsDatabasesDocumentsRunQueryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RunQueryResponse) The response message.
      """
      config = self.GetMethodConfig('RunQuery')
      return self._RunMethod(
          config, request, global_params=global_params)

    RunQuery.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/documents/{documentsId}/{documentsId1}:runQuery',
        http_method=u'POST',
        method_id=u'firestore.projects.databases.documents.runQuery',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}:runQuery',
        request_field=u'runQueryRequest',
        request_type_name=u'FirestoreProjectsDatabasesDocumentsRunQueryRequest',
        response_type_name=u'RunQueryResponse',
        supports_download=False,
    )

    def Write(self, request, global_params=None):
      r"""Streams batches of document updates and deletes, in order.

      Args:
        request: (FirestoreProjectsDatabasesDocumentsWriteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (WriteResponse) The response message.
      """
      config = self.GetMethodConfig('Write')
      return self._RunMethod(
          config, request, global_params=global_params)

    Write.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/documents:write',
        http_method=u'POST',
        method_id=u'firestore.projects.databases.documents.write',
        ordered_params=[u'database'],
        path_params=[u'database'],
        query_params=[],
        relative_path=u'v1/{+database}/documents:write',
        request_field=u'writeRequest',
        request_type_name=u'FirestoreProjectsDatabasesDocumentsWriteRequest',
        response_type_name=u'WriteResponse',
        supports_download=False,
    )

  class ProjectsDatabasesOperationsService(base_api.BaseApiService):
    """Service class for the projects_databases_operations resource."""

    _NAME = u'projects_databases_operations'

    def __init__(self, client):
      super(FirestoreV1.ProjectsDatabasesOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (FirestoreProjectsDatabasesOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/operations/{operationsId}:cancel',
        http_method=u'POST',
        method_id=u'firestore.projects.databases.operations.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:cancel',
        request_field=u'googleLongrunningCancelOperationRequest',
        request_type_name=u'FirestoreProjectsDatabasesOperationsCancelRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (FirestoreProjectsDatabasesOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/operations/{operationsId}',
        http_method=u'DELETE',
        method_id=u'firestore.projects.databases.operations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'FirestoreProjectsDatabasesOperationsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (FirestoreProjectsDatabasesOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'firestore.projects.databases.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'FirestoreProjectsDatabasesOperationsGetRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (FirestoreProjectsDatabasesOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}/operations',
        http_method=u'GET',
        method_id=u'firestore.projects.databases.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+name}/operations',
        request_field='',
        request_type_name=u'FirestoreProjectsDatabasesOperationsListRequest',
        response_type_name=u'GoogleLongrunningListOperationsResponse',
        supports_download=False,
    )

  class ProjectsDatabasesService(base_api.BaseApiService):
    """Service class for the projects_databases resource."""

    _NAME = u'projects_databases'

    def __init__(self, client):
      super(FirestoreV1.ProjectsDatabasesService, self).__init__(client)
      self._upload_configs = {
          }

    def ExportDocuments(self, request, global_params=None):
      r"""Exports a copy of all or a subset of documents from Google Cloud Firestore.
to another storage system, such as Google Cloud Storage. Recent updates to
documents may not be reflected in the export. The export occurs in the
background and its progress can be monitored and managed via the
Operation resource that is created. The output of an export may only be
used once the associated operation is done. If an export operation is
cancelled before completion it may leave partial data behind in Google
Cloud Storage.

      Args:
        request: (FirestoreProjectsDatabasesExportDocumentsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('ExportDocuments')
      return self._RunMethod(
          config, request, global_params=global_params)

    ExportDocuments.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}:exportDocuments',
        http_method=u'POST',
        method_id=u'firestore.projects.databases.exportDocuments',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:exportDocuments',
        request_field=u'googleFirestoreAdminV1ExportDocumentsRequest',
        request_type_name=u'FirestoreProjectsDatabasesExportDocumentsRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def ImportDocuments(self, request, global_params=None):
      r"""Imports documents into Google Cloud Firestore. Existing documents with the.
same name are overwritten. The import occurs in the background and its
progress can be monitored and managed via the Operation resource that is
created. If an ImportDocuments operation is cancelled, it is possible
that a subset of the data has already been imported to Cloud Firestore.

      Args:
        request: (FirestoreProjectsDatabasesImportDocumentsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('ImportDocuments')
      return self._RunMethod(
          config, request, global_params=global_params)

    ImportDocuments.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/databases/{databasesId}:importDocuments',
        http_method=u'POST',
        method_id=u'firestore.projects.databases.importDocuments',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:importDocuments',
        request_field=u'googleFirestoreAdminV1ImportDocumentsRequest',
        request_type_name=u'FirestoreProjectsDatabasesImportDocumentsRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(FirestoreV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (FirestoreProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}',
        http_method=u'GET',
        method_id=u'firestore.projects.locations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'FirestoreProjectsLocationsGetRequest',
        response_type_name=u'Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (FirestoreProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations',
        http_method=u'GET',
        method_id=u'firestore.projects.locations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+name}/locations',
        request_field='',
        request_type_name=u'FirestoreProjectsLocationsListRequest',
        response_type_name=u'ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(FirestoreV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }