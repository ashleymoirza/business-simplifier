/**
 * General utility helpers
 */

/** Format a date string for display */
export function formatDate(dateStr) {
  return new Date(dateStr).toLocaleDateString('en-ZA', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
}

/** Join class names, filtering falsy values */
export function cn(...classes) {
  return classes.filter(Boolean).join(' ');
}