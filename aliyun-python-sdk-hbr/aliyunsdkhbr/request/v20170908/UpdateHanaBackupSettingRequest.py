# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class UpdateHanaBackupSettingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdateHanaBackupSetting','hbr')
		self.set_protocol_type('https')

	def get_LogBackupParameterFile(self):
		return self.get_query_params().get('LogBackupParameterFile')

	def set_LogBackupParameterFile(self,LogBackupParameterFile):
		self.add_query_param('LogBackupParameterFile',LogBackupParameterFile)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_LogBackupUsingBackint(self):
		return self.get_query_params().get('LogBackupUsingBackint')

	def set_LogBackupUsingBackint(self,LogBackupUsingBackint):
		self.add_query_param('LogBackupUsingBackint',LogBackupUsingBackint)

	def get_LogBackupTimeout(self):
		return self.get_query_params().get('LogBackupTimeout')

	def set_LogBackupTimeout(self,LogBackupTimeout):
		self.add_query_param('LogBackupTimeout',LogBackupTimeout)

	def get_CatalogBackupUsingBackint(self):
		return self.get_query_params().get('CatalogBackupUsingBackint')

	def set_CatalogBackupUsingBackint(self,CatalogBackupUsingBackint):
		self.add_query_param('CatalogBackupUsingBackint',CatalogBackupUsingBackint)

	def get_DatabaseName(self):
		return self.get_query_params().get('DatabaseName')

	def set_DatabaseName(self,DatabaseName):
		self.add_query_param('DatabaseName',DatabaseName)

	def get_DataBackupParameterFile(self):
		return self.get_query_params().get('DataBackupParameterFile')

	def set_DataBackupParameterFile(self,DataBackupParameterFile):
		self.add_query_param('DataBackupParameterFile',DataBackupParameterFile)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_EnableAutoLogBackup(self):
		return self.get_query_params().get('EnableAutoLogBackup')

	def set_EnableAutoLogBackup(self,EnableAutoLogBackup):
		self.add_query_param('EnableAutoLogBackup',EnableAutoLogBackup)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_CatalogBackupParameterFile(self):
		return self.get_query_params().get('CatalogBackupParameterFile')

	def set_CatalogBackupParameterFile(self,CatalogBackupParameterFile):
		self.add_query_param('CatalogBackupParameterFile',CatalogBackupParameterFile)