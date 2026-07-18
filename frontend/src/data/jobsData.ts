import type { Job, Benefit, Testimonial } from "../types";

export const jobsData: Job[] = [
  {
    id: "1",
    title: "Senior Machine Learning Architect",
    department: "Engineering",
    location: "Remote",
    type: "Full-time",
  },
  {
    id: "2",
    title: "Principal Product Designer",
    department: "Product Design",
    location: "Hyderabad",
    type: "Full-time",
  },
  {
    id: "3",
    title: "Senior Frontend Engineer (React)",
    department: "Engineering",
    location: "Remote",
    type: "Full-time",
  },
  {
    id: "4",
    title: "Lead AI Researcher",
    department: "AI Research",
    location: "San Francisco",
    type: "Full-time",
  },
  {
    id: "5",
    title: "Product Manager - AI Platform",
    department: "Product Management",
    location: "Hyderabad",
    type: "Full-time",
  },
  {
    id: "6",
    title: "Growth Marketing Manager",
    department: "Marketing",
    location: "Remote",
    type: "Full-time",
  }
];

export const benefitsData: Benefit[] = [
  {
    id: "b1",
    title: "Any Time",
    description: "Work in your free time",
    iconName: "ShieldAlert", // Standard icons, we'll map them in UI
  },
  {
    id: "b2",
    title: "Work Anywhere",
    description: "Flexible remote-first infrastructure with luxury coworking passes and home office stipends.",
    iconName: "MapPin",
  },
  {
    id: "b3",
    title: "Health & Wellness",
    description: "Premium health insurance, mental health support, and gym memberships for your physical well-being.",
    iconName: "Activity",
  },
  {
    id: "b4",
    title: "Continuous Growth",
    description: "Generous learning stipend, mentorship program, and fast-track career path in a rapidly scaling AI startup.",
    iconName: "TrendingUp",
  }
];

export const testimonialsData: Testimonial[] = [
  {
    id: "t1",
    quote: "Pranaga is where the most ambitious ideas meet the most rigorous execution. I've never felt more supported in my research.",
    author: "Marcus Thorne",
    role: "SENIOR AI RESEARCHER",
    avatar: "/assets/avatar_marcus.png",
  },
  {
    id: "t2",
    quote: "The design culture here is exceptional. We don't just 'make it pretty'; we design the logic of interaction for the next century.",
    author: "Sarah Jenkins",
    role: "DESIGN LEAD",
    avatar: "/assets/avatar_sarah.png",
  },
  {
    id: "t3",
    quote: "Transparency isn't just a buzzword here. Every team member has access to executive meetings and strategic planning.",
    author: "David Chen",
    role: "PRODUCT MANAGER",
    avatar: "/assets/avatar_david.png",
  }
];
