export interface Job {
  id: string;
  title: string;
  department: string;
  location: string;
  type: string;
}

export interface Testimonial {
  id: string;
  quote: string;
  author: string;
  role: string;
  avatar: string;
}

export interface Benefit {
  id: string;
  title: string;
  description: string;
  iconName: string;
}
