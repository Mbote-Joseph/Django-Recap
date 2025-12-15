from classroom.views import ClassRoomDetailsView, ClassroomCreate, ClassroomListView
# Copyright 2025 josephmbote
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.urls import path
from .views import ClassroomDelete, ClassroomEdit, ClassroomListView, ClassRoomDetailsView


urlpatterns = [
    path('', ClassroomListView.as_view(), name="classroom" ),
    path('/<int:pk>', ClassRoomDetailsView.as_view(), name="classroom.details"),
    path('/add', ClassroomCreate.as_view(), name ="class.add"),
    path('/<int:pk>/edit', ClassroomEdit.as_view(), name="classroom.edit"),
    path('/<int:pk>/delete', ClassroomDelete.as_view(), name="classroom.delete")
] 