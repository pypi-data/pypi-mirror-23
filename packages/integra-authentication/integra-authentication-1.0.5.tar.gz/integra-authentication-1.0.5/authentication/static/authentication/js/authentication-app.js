// Login App
// Author : Partha

AuthApp = angular.module('Authentication', ['ngCookies']);
AuthApp.config(['$interpolateProvider','$httpProvider', '$compileProvider',
    function($interpolateProvider,$httpProvider,$compileProvider) {
        $compileProvider.debugInfoEnabled(false); 
        $httpProvider.useApplyAsync(true);
        $interpolateProvider.startSymbol('{[');
        $interpolateProvider.endSymbol(']}');
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/json;odata=verbose'; 
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';       
}]);
AuthApp.run(['$http','$cookies',
    function($http, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.xsrfCookieName = 'csrftoken';
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);


AuthApp.factory('AuthAPI', function ($http) {
    
    var userLogin = function(creds){
        // For sending ajax to login the user
        // @{username:'', password:''} => creds

        return $http({ 
            method: "POST", 
            url: '/auth/login/',
            headers: {
                'content-type': 'application/x-www-form-urlencoded'
            },
            data: $.param(creds)
        });
    };

    var userRegister = function(UserData){
        // For registering the user 
        // {'username':'', first_name:'', email:'', password:''} => UserData

        return $http({ 
            method: "POST", 
            url: '/auth/register/',
            headers: {
                'content-type': 'application/x-www-form-urlencoded'
            },
            data: $.param(UserData)
        });
    };

    // Exposing the funcationality
    return {
        'userLogin': userLogin,
        'userRegister': userRegister, 
    }
});

// Controllers
AuthApp.controller('LoginRegisterController',['$scope','$rootScope','$http', '$sce', '$compile', '$q', 'AuthAPI',
    function($scope,$rootScope, $http, $sce, $compile, $q, AuthAPI){
        
        // Initializing the Login and Register data holder
        $scope.login = {};
        $scope.register = {};

        // User Actions
        $scope.userLogin = function() {
            // Login the user
            // @$scope.login
            AuthAPI.userLogin($scope.login).then(function(data){
                // onSuccess
                data = data.data;
                if (data.status == "success"){
                    window.location.href = "/";
                } else {
                    alert(data.message);
                }
            }, function(data){
                // onFailure
                alert("Something went wrong");                
            });
        };

        $scope.userRegister = function() {
            // Register the user
            // @$scope.register
            if ($scope.register.password == $scope.register.confirm_password){         
                AuthAPI.userRegister($scope.register).then(function(data){
                    // onSuccess
                    data = data.data;
                    if (data.status == "success"){
                        alert("Please Login to Continue");
                        $('#login-form-link').trigger('click');
                        $scope.register = {};
                    } else {
                        alert(data.message);
                    }
                }, function(data){
                    // onFailure
                    alert("Something went wrong");
                });
            } else {
                alert("Password and Confirm Password must be same");
            }
        };
}]);


// Login Panel 
// Ref: https://bootsnipp.com/snippets/featured/login-and-register-tabbed-form
$(document).ready(function(){
    $(function() {
        $('#login-form-link').click(function(e) {
            $("#login-form").delay(100).fadeIn(100);
            $("#register-form").fadeOut(100);
            $('#register-form-link').removeClass('active');
            $(this).addClass('active');
            e.preventDefault();
        });
        $('#register-form-link').click(function(e) {
            $("#register-form").delay(100).fadeIn(100);
            $("#login-form").fadeOut(100);
            $('#login-form-link').removeClass('active');
            $(this).addClass('active');
            e.preventDefault();
        });

    });
});