from examples.ex25_studentManagement.repository.GradeCSVFileRepository import GradeCSVFileRepository
from examples.ex25_studentManagement.repository.StudentCSVFileRepository import StudentCSVFileRepository

from examples.ex25_studentManagement.domain.GradeValidator import GradeValidator 
from examples.ex25_studentManagement.domain.StudentValidator import StudentValidator
from examples.ex25_studentManagement.controller.StudentController import StudentController
from examples.ex25_studentManagement.controller.GradeController import GradeController
from examples.ex25_studentManagement.ui.Console import ConsoleUI
from examples.ex25_studentManagement.repository.StudentPickleFileRepository import StudentPickleFileRepository
from examples.ex25_studentManagement.repository.GradeRepository import GradeRepository
from examples.ex25_studentManagement.repository.GradePickleFileRepository import GradePickleFileRepository

"""
    1. Set up entity validators
"""
studentValidator = StudentValidator()
gradeValidator = GradeValidator()

"""
    2. Initialize the repositories
"""
studentRepo = StudentCSVFileRepository("students.txt")
# studentRepo = StudentPickleFileRepository()
gradeRepo = GradeCSVFileRepository(studentRepo, "grades.txt")
# gradeRepo = GradePickleFileRepository(studentRepo)

"""
    3. Initialize GRASP controllers
"""
studentController = StudentController(studentValidator, studentRepo)
gradeController = GradeController(gradeRepo, gradeValidator, studentRepo)

"""
    4. Start up the UI
"""
ui = ConsoleUI(studentController, gradeController)
ui.startUI()