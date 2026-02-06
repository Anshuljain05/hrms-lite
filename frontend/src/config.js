/**
 * Frontend Configuration
 * Uses environment variables for API configuration
 */

// Environment: development, staging, production
const ENVIRONMENT = import.meta.env.VITE_ENVIRONMENT || 'development';

// API Base URL - Configured via environment variable VITE_API_URL
// Defaults based on environment:
// - development: http://localhost:8000
// - staging: https://api-staging.example.com
// - production: https://api.example.com
const API_BASE_URL = import.meta.env.VITE_API_URL || getDefaultApiUrl(ENVIRONMENT);

/**
 * Get default API URL based on environment
 * @param {string} env - Current environment
 * @returns {string} API URL
 */
function getDefaultApiUrl(env) {
  const defaults = {
    development: 'http://localhost:8000',
    staging: import.meta.env.VITE_API_STAGING_URL || 'https://api-staging.example.com',
    production: import.meta.env.VITE_API_PROD_URL || 'https://api.example.com'
  };
  
  return defaults[env] || defaults.development;
}

// Export configuration
export const API_URL = API_BASE_URL.endsWith('/') ? API_BASE_URL.slice(0, -1) : API_BASE_URL;
export const APP_ENVIRONMENT = ENVIRONMENT;

// API Endpoints
export const API_ENDPOINTS = {
  employees: {
    list: '/api/employees',
    create: '/api/employees',
    get: (id) => `/api/employees/${id}`,
    update: (id) => `/api/employees/${id}`,
    delete: (id) => `/api/employees/${id}`
  },
  attendance: {
    list: '/api/attendance',
    create: '/api/attendance',
    getByEmployee: (employeeId) => `/api/attendance/employee/${employeeId}`,
    get: (id) => `/api/attendance/${id}`,
    update: (id) => `/api/attendance/${id}`,
    delete: (id) => `/api/attendance/${id}`
  }
};

// Request timeout (in milliseconds)
export const REQUEST_TIMEOUT = parseInt(
  import.meta.env.VITE_REQUEST_TIMEOUT || 30000,
  10
);

// Log level: 'error', 'warn', 'info', 'debug'
export const LOG_LEVEL = import.meta.env.VITE_LOG_LEVEL || (
  ENVIRONMENT === 'production' ? 'error' : 'debug'
);

// Debug mode
export const DEBUG = ENVIRONMENT !== 'production' && (
  import.meta.env.VITE_DEBUG === 'true'
);

// Development checks
if (DEBUG) {
  console.debug('[Config]', {
    environment: ENVIRONMENT,
    apiUrl: API_URL,
    requestTimeout: REQUEST_TIMEOUT,
    logLevel: LOG_LEVEL
  });
}
