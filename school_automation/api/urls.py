from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

router = DefaultRouter()

# Registering all the viewsets
router.register(r'users', UserModelViewSet, basename="users")
router.register(r'filials', BranchModelViewSet, basename="filials")
router.register(r'rooms', RoomModelViewSet, basename="rooms")
router.register(r'discounts', DicountModelViewSet, basename="discounts")
router.register(r'ads', AdvertisementModelViewSet, basename="ads")
router.register(r'lessons', LessonModelViewSet, basename="lessons")
router.register(r'students', StudentModelViewSet, basename="students")
router.register(r'teachers', TeacherModelViewSet, basename="teachers")
router.register(r'staff_users', StuffUserModelViewSet, basename="staff_users")
router.register(r'groups', GroupModelViewSet, basename="groups")
router.register(r'absences', AbsenceModelViewSet, basename="absences")
router.register(r'group_schedules', GroupScheduleModelViewSet, basename="group_schedules")
router.register(r'student_payments', StudentPaymentModelViewSet, basename="student_payments")
router.register(r'teacher_salary_payments', TeacherSalaryPaymentModelViewSet, basename="teacher_salary_payments")
router.register(r'staff_user_salaries', StaffUserSalaryModelViewSet, basename="staff_user_salaries")
router.register(r'new_students', NewStudentFormModelViewSet, basename="new_students")
router.register(r'expenses', ExpenseModelViewSet, basename="expenses")

urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('teachers/teachers_salary/<int:teacher_id>', TeacherModelViewSet.as_view({'get': 'teachers_salary'}), name="teachers_salary"),
    path('new_students/income_outcome/<int:year>', NewStudentFormModelViewSet.as_view({'get': 'income_outcome'}), name="income_outcome"),
]