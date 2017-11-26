angular.module('patientPapers', [])
    .controller('PatientPapersController', function ($scope, $http) {
        var patientPapers = this

        var baseUrl = 'http://patientpapers.com:5000';

        $scope.search = {
            q: ""
        };

        $scope.patientList = [];

        this.patient = {
            name: 'Name Surname'
        };

        function passOutSearchResult(patients) {
            $scope.patientList = [];
            for (i = 0; i < patients.length; i++) {
                var patient = patients[i]; 
                $scope.patientList.push(
                    {
                        'forename': patient['name'],
                        'surname': patient['surname'],
                        'name': patient['name'] + ' ' + patient['surname'],
                        'gender': patient['gender'],
                        'birthdate': patient['birthdate']
                    }
                )
            }
            console.log(this.patientList);
        }

        $scope.getPatient = function () {
            console.log('Searching for: ' + $scope.search.q)
            $http({
                method: 'GET',
                url: baseUrl + '/search',
                params: {
                    'q': $scope.search.q
                }
            }).then(function successCallback(response) {
                console.log(response);
                passOutSearchResult(response.data);
            }, function errorCallback(response) {
                console.log(response);
            });
        };
    });
